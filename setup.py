from distutils.core import setup
from Cython.Build import cythonize
import numpy

ext_options = {"compiler_directives": {"profile": True}, "annotate": True}  # , "zip_safe": False}
setup(
    include_dirs=[numpy.get_include()],
    ext_modules=cythonize("multcython.pyx", **ext_options)
)
