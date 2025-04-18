import tensorflow as tf
from tensorflow.python.framework import ops
import sys
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Load the custom op shared library
sampling_module = tf.load_op_library(os.path.join(BASE_DIR, 'tf_sampling_so.so'))

def prob_sample(inp, inpr):
    '''
    input:
        batch_size * ncategory float32
        batch_size * npoints   float32
    returns:
        batch_size * npoints   int32
    '''
    return sampling_module.prob_sample(inp, inpr)

ops.NoGradient('ProbSample')

def gather_point(inp, idx):
    '''
    input:
        batch_size * ndataset * 3   float32
        batch_size * npoints        int32
    returns:
        batch_size * npoints * 3    float32
    '''
    return sampling_module.gather_point(inp, idx)

@tf.RegisterGradient('GatherPoint')
def _gather_point_grad(op, out_g):
    inp = op.inputs[0]
    idx = op.inputs[1]
    return [sampling_module.gather_point_grad(inp, idx, out_g), None]

def farthest_point_sample(npoint, inp):
    '''
    input:
        int32
        batch_size * ndataset * 3   float32
    returns:
        batch_size * npoint         int32
    '''
    return sampling_module.farthest_point_sample(inp, npoint)

ops.NoGradient('FarthestPointSample')

if __name__ == '__main__':
    np.random.seed(100)
    triangles = np.random.rand(1, 5, 3, 3).astype('float32')

    # Using eager execution, which is the default in TensorFlow 2.x
    inp = tf.constant(triangles)
    tria = inp[:, :, 0, :]
    trib = inp[:, :, 1, :]
    tric = inp[:, :, 2, :]

    areas = tf.sqrt(tf.reduce_sum(tf.cross(trib - tria, tric - tria)**2, 2) + 1e-9)
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
    print("pt_sample: ", pt_sample)

    reduced_sample = gather_point(pt_sample, farthest_point_sample(1024, pt_sample))
    print("reduced_sample: ", reduced_sample)

    # Evaluate and save the output
    ret = reduced_sample.numpy()  # In eager execution, use .numpy() to evaluate tensors
    print(ret.shape, ret.dtype)

    import pickle
    with open('1.pkl', 'wb') as f:
        pickle.dump(ret, f, protocol=pickle.HIGHEST_PROTOCOL)
