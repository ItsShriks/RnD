from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension
import os
import subprocess

# Define the extension
ext_modules = [
    Extension(
        name="tf_sampling_so",
        sources=["tf_sampling.cpp", "tf_sampling.cu"],
        include_dirs=[os.path.join(os.environ['CUDA_HOME'], 'include')],
        library_dirs=[os.path.join(os.environ['CUDA_HOME'], 'lib64')],
        libraries=['cudart'],
        extra_compile_args=["-O2", "-DGOOGLE_CUDA=1", "-x", "cu", "-Xcompiler", "-fPIC"],
        language="c++",
    )
]

# Setup
setup(
    name='tf_sampling',
    ext_modules=cythonize(ext_modules),
)
