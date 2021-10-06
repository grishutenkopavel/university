from setuptools import setup
from Cython.Build import cythonize

setup(
    name='integrate app',
    ext_modules=cythonize("cint.pyx"),
    zip_safe=False,
)