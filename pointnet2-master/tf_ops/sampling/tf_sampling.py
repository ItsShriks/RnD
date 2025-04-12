import tensorflow as tf
from tensorflow.python.framework import ops
import numpy as np
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sampling_module = tf.load_op_library(os.path.join(BASE_DIR, 'tf_sampling_so.so'))

# Custom ops
def prob_sample(inp, inpr):
    '''
    Args:
        inp: batch_size x ncategory float32
        inpr: batch_size x npoints float32
    Returns:
        batch_size x npoints int32
    '''
    return sampling_module.prob_sample(inp, inpr)

ops.NoGradient('ProbSample')

def gather_point(inp, idx):
    '''
    Args:
        inp: batch_size x ndataset x 3 float32
        idx: batch_size x npoints int32
    Returns:
        batch_size x npoints x 3 float32
    '''
    return sampling_module.gather_point(inp, idx)

@tf.RegisterGradient('GatherPoint')
def _gather_point_grad(op, grad_output):
    inp = op.inputs[0]
    idx = op.inputs[1]
    return [sampling_module.gather_point_grad(inp, idx, grad_output), None]

def farthest_point_sample(npoint, inp):
    '''
    Args:
        npoint: int32
        inp: batch_size x ndataset x 3 float32
    Returns:
        batch_size x npoint int32
    '''
    return sampling_module.farthest_point_sample(inp, npoint)

ops.NoGradient('FarthestPointSample')


# Test main
if __name__ == '__main__':
    tf.compat.v1.disable_eager_execution()  # Required for running sessions in TF2
    np.random.seed(100)
    triangles = np.random.rand(1, 5, 3, 3).astype('float32')

    with tf.device('/gpu:0'):
        inp = tf.constant(triangles)
        tria = inp[:, :, 0, :]
        trib = inp[:, :, 1, :]
        tric = inp[:, :, 2, :]

        areas = tf.sqrt(tf.reduce_sum(tf.linalg.cross(trib - tria, tric - tria) ** 2, axis=2) + 1e-9)
        randomnumbers = tf.random.uniform((1, 8192))
        triids = prob_sample(areas, randomnumbers)

        tria_sample = gather_point(tria, triids)
        trib_sample = gather_point(trib, triids)
        tric_sample = gather_point(tric, triids)

        us = tf.random.uniform((1, 8192))
        vs = tf.random.uniform((1, 8192))
        uplusv = 1 - tf.abs(us + vs - 1)
        uminusv = us - vs
        us = (uplusv + uminusv) * 0.5
        vs = (uplusv - uminusv) * 0.5

        pt_sample = tria_sample + (trib_sample - tria_sample) * tf.expand_dims(us, -1) + (tric_sample - tria_sample) * tf.expand_dims(vs, -1)
        reduced_sample = gather_point(pt_sample, farthest_point_sample(1024, pt_sample))

    with tf.compat.v1.Session() as sess:
        ret = sess.run(reduced_sample)

    print("Sampled Points Shape:", ret.shape)
    print("Sampled Points Type:", ret.dtype)

    import pickle
    with open('1.pkl', 'wb') as f:
        pickle.dump(ret, f, protocol=pickle.HIGHEST_PROTOCOL)
