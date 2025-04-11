from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig
import tensorflow as tf

class BuildExtension(build_ext_orig):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = {
                'gcc': ['-std=c++11'],
                'nvcc': [
                    '-arch=sm_60', '--ptxas-options=-v', '-c', '--compiler-options', "'-fPIC'"
                ]
            }
        super().build_extensions()

_ext = Extension(
    '_tf_grouping_so',
    sources=['grouping.cpp', 'grouping.cu'],
    extra_compile_args=['-std=c++11'],
    include_dirs=[tf.sysconfig.get_include(), tf.sysconfig.get_include() + '/external/nsync/public'],
    library_dirs=[tf.sysconfig.get_lib()],
    language='c++'
)

setup(
    name='tf_grouping',
    ext_modules=[_ext],
    cmdclass={'build_ext': BuildExtension},
)
