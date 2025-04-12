import tensorflow as tf
from tensorflow.python.framework import ops
import sys
import os
import numpy as np
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
grouping_module = tf.load_op_library(os.path.join(BASE_DIR, 'tf_grouping_so.so'))

def query_ball_point(radius, nsample, xyz1, xyz2):
    return grouping_module.query_ball_point(xyz1, xyz2, radius, nsample)

ops.NoGradient('QueryBallPoint')

def select_top_k(k, dist):
    return grouping_module.selection_sort(dist, k)

ops.NoGradient('SelectionSort')

def group_point(points, idx):
    return grouping_module.group_point(points, idx)

@tf.RegisterGradient('GroupPoint')
def _group_point_grad(op, grad_out):
    points = op.inputs[0]
    idx = op.inputs[1]
    return [grouping_module.group_point_grad(points, idx, grad_out), None]

def knn_point(k, xyz1, xyz2):
    '''
    Input:
        k: int — top k
        xyz1: (b, ndataset, c)
        xyz2: (b, npoint, c)
    Returns:
        val: (b, npoint, k) distances
        idx: (b, npoint, k) indices of k-NN
    '''
    b = tf.shape(xyz1)[0]
    n = tf.shape(xyz1)[1]
    c = tf.shape(xyz1)[2]
    m = tf.shape(xyz2)[1]

    xyz1_expand = tf.tile(tf.reshape(xyz1, (b, 1, n, c)), [1, m, 1, 1])
    xyz2_expand = tf.tile(tf.reshape(xyz2, (b, m, 1, c)), [1, 1, n, 1])
    dist = tf.reduce_sum((xyz1_expand - xyz2_expand) ** 2, axis=-1)

    outi, out = select_top_k(k, dist)
    idx = tf.slice(outi, [0, 0, 0], [-1, -1, k])
    val = tf.slice(out, [0, 0, 0], [-1, -1, k])

    return val, idx

# === Main Test ===
if __name__ == '__main__':
    tf.compat.v1.disable_eager_execution()
    knn = True

    np.random.seed(100)
    pts = np.random.random((32, 512, 64)).astype('float32')
    tmp1 = np.random.random((32, 512, 3)).astype('float32')
    tmp2 = np.random.random((32, 128, 3)).astype('float32')

    with tf.device('/cpu:0'):  # change to '/gpu:0' if running with GPU
        points = tf.constant(pts)
        xyz1 = tf.constant(tmp1)
        xyz2 = tf.constant(tmp2)
        radius = 0.1
        nsample = 64

        if knn:
            _, idx = knn_point(nsample, xyz1, xyz2)
            grouped_points = group_point(points, idx)
        else:
            idx, _ = query_ball_point(radius, nsample, xyz1, xyz2)
            grouped_points = group_point(points, idx)

    with tf.compat.v1.Session() as sess:
        now = time.time()
        for _ in range(100):
            ret = sess.run(grouped_points)
        print("Elapsed time:", time.time() - now)
        print("Output shape:", ret.shape)
        print("Output dtype:", ret.dtype)
        print("Output sample:", ret[0, 0, 0])  # Optional
