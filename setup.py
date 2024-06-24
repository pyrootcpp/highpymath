# setup.py
from setuptools import setup, Extension, find_packages
from setuptools_rust import RustExtension
from Cython.Build import cythonize

def read(file):
    with open(file, 'r') as f:
        return f.read()

setup(
    name="highpymath",
    version="0.1.1",
    packages=find_packages(),
    description="High Quality Math library for Python",
    author="pyrootcpp",
    author_email="pyrootcpp@outlook.de",
    long_description=read('README.rst'),
    license=read('LICENSE'),
    rust_extensions=[RustExtension("highpymath", "Cargo.toml", binding="pyo3")],
    ext_modules=cythonize("highpymath/math.pyx"),
    zip_safe=False,
)