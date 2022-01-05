"""
    from this beautiful url
    https://rich.readthedocs.io/en/latest/traceback.html

    file metadata:
        path: core/__init__.py

"""

from rich.traceback import install
install(
    show_locals=True,
    word_wrap=True
)

from ._json import *
from ._rich import *
from ._collections import *

