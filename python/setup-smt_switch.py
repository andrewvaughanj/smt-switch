from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("smt_switch.pyx", language_level=3))
