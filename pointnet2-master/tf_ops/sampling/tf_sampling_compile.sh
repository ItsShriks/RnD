#!/bin/bash

# CUDA 11.8
/usr/local/cuda-11.8/bin/nvcc tf_sampling_g.cu -o tf_sampling_g.cu.o -c -O2 -DGOOGLE_CUDA=1 -x cu -Xcompiler -fPIC

# Get the TensorFlow include path for Python 3.x
TF_INCLUDE_PATH=$(python3 -c "import tensorflow as tf; print(tf.sysconfig.get_include())")

# TF1.2
g++ -std=c++11 tf_sampling.cpp tf_sampling_g.cu.o -o tf_sampling_so.so -shared -fPIC -I $TF_INCLUDE_PATH -I /usr/local/cuda-11.8/include -lcudart -L /usr/local/cuda-11.8/lib64/ -O2 -D_GLIBCXX_USE_CXX11_ABI=0

# TF1.4 (optional, if you need to support TF1.4)
#g++ -std=c++11 tf_sampling.cpp tf_sampling_g.cu.o -o tf_sampling_so.so -shared -fPIC -I $TF_INCLUDE_PATH -I /usr/local/cuda-11.8/include -I /usr/local/lib/python3.8/dist-packages/tensorflow/include/external/nsync/public -lcudart -L /usr/local/cuda-11.8/lib64/ -L/usr/local/lib/python3.8/dist-packages/tensorflow -ltensorflow_framework -O2 -D_GLIBCXX_USE_CXX11_ABI=0
