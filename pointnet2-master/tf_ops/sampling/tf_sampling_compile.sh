#!/bin/bash

# Define CUDA path (based on your env)
CUDA_PATH=/home/jovyan/.local/opt/conda/envs/itshriks

# Compile the CUDA code
$CUDA_PATH/bin/nvcc tf_sampling.cu -o tf_sampling.cu.o -c -O2 -DGOOGLE_CUDA=1 -x cu -Xcompiler -fPIC

# Compile the shared object using g++
g++ -std=c++11 tf_sampling.cpp tf_sampling.cu.o -o tf_sampling_so.so -shared -fPIC \
    -I$CUDA_PATH/include \
    -I$CUDA_PATH/lib/python3.*/site-packages/tensorflow/include \
    -L$CUDA_PATH/lib \
    -L$CUDA_PATH/lib64 \
    -lcudart
