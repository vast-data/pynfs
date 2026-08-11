import os as _os, sys as _sys
# Python 3: make the package directory importable so the historic bare
# (implicit-relative) imports such as ``import nlm_const`` keep working.
_sys.path.insert(1, _os.path.dirname(_os.path.abspath(__file__)))
