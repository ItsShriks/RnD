import tensorflow as tf
from tensorflow.python.framework import ops
import numpy as np
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
interpolate_module = tf.load_op_library(os.path.join(BASE_DIR, 'tf_interpolate_so.so'))

# Wrapper for three_nn
def three_nn(xyz1, xyz2):
    '''
    Args:
        xyz1: (b, n, 3) float32 — unknown points
        xyz2: (b, m, 3) float32 — known points
    Returns:
        dist: (b, n, 3) float32 — distances to known points
        idx: (b, n, 3) int32 — indices of the nearest neighbors
    '''
    return interpolate_module.three_nn(xyz1, xyz2)

ops.NoGradient('ThreeNN')

# Wrapper for three_interpolate
def three_interpolate(points, idx, weight):
    '''
    Args:
        points: (b, m, c) float32 — features of known points
        idx: (b, n, 3) int32 — neighbor indices for each unknown point
        weight: (b, n, 3) float32 — interpolation weights
    Returns:
        out: (b, n, c) float32 — interpolated feature values
    '''
    return interpolate_module.three_interpolate(points, idx, weight)

@tf.RegisterGradient('ThreeInterpolate')
def _three_interpolate_grad(op, grad_out):
    points = op.inputs[0]
    idx = op.inputs[1]
    weight = op.inputs[2]
    return [interpolate_module.three_interpolate_grad(points, idx, weight, grad_out), None, None]


# Test code
if __name__ == '__main__':
    tf.compat.v1.disable_eager_execution()  # Enable session in TF2

    np.random.seed(100)
    pts = np.random.random((32, 128, 64)).astype('float32')     # (batch_size, known_points, channels)
    tmp1 = np.random.random((32, 512, 3)).astype('float32')     # (batch_size, unknown_points, 3)
    tmp2 = np.random.random((32, 128, 3)).astype('float32')     # (batch_size, known_points, 3)

    with tf.device('/cpu:0'):
        points = tf.constant(pts)
        xyz1 = tf.constant(tmp1)
        xyz2 = tf.constant(tmp2)

        dist, idx = three_nn(xyz1, xyz2)                         # Find 3-NN for unknown points in known points
        weight = tf.ones_like(dist) / 3.0                        # Uniform weights
        interpolated_points = three_interpolate(points, idx, weight)

    with tf.compat.v1.Session() as sess:
        start_time = time.time()
        for _ in range(100):
            ret = sess.run(interpolated_points)
        end_time = time.time()

        print("Elapsed Time (100 runs):", end_time - start_time)
        print("Output Shape:", ret.shape)
        print("Output Type:", ret.dtype)
