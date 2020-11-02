from distutils.core import setup # old version
#from setuptools import setup # my new version
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

extensions = [
  Extension('cs231n.im2col_cython', ['im2col_cython.pyx'],
            include_dirs = [numpy.get_include()]
  ),
]

setup(
    ext_modules = cythonize(extensions),
)
