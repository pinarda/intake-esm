#!/usr/bin/env python
"""Top-level module for intake_cesm."""
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from .core import CesmSource, CesmMetadataStoreCatalog
from .manage_collections import CESMCollections
