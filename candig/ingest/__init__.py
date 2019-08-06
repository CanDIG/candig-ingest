"""
Import the version of the package
"""

__version__ = "undefined"
try:
    from . import _version
    __version__ = _version.version
except ImportError:
    pass
