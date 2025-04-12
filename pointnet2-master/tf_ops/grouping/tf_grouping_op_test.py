import tensorflow as tf
import numpy as np
from tf_grouping import query_ball_point, group_point

class GroupPointTest(tf.test.TestCase):
    def test_grad(self):
        tf.compat.v1.disable_eager_execution()  # Ensure TF1 behavior for gradient tests
        with tf.device('/gpu:0'):
            points = tf.constant(np.random.random((1, 128, 16)).astype('float32'))
            xyz1 = tf.constant(np.random.random((1, 128, 3)).astype('float32'))
            xyz2 = tf.constant(np.random.random((1, 8, 3)).astype('float32'))
            radius = 0.3
            nsample = 32
            idx, pts_cnt = query_ball_point(radius, nsample, xyz1, xyz2)
            grouped_points = group_point(points, idx)

        with self.session():
            print("---- Going to compute gradient error")
            err = tf.test.compute_gradient_error(
                points, (1, 128, 16),
                grouped_points, (1, 8, 32, 16)
            )
            print("Gradient error:", err)
            self.assertLess(err, 1e-4)

if __name__ == '__main__':
    tf.test.main()
