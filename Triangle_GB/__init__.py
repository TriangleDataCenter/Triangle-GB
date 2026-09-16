# Triangle_GB/__init__.py
"""
``Triangle_GB`` : fast time-delay-interferometry (TDI) response model for
Galactic binaries (GBs), supporting arbitrary detector orbit and arbitrary
TDI combination.

Public classes (module :mod:`Triangle_GB.TDIFly`):

    ``TDIFly``
        Sparse-sampling ("TDI on the fly") response generator for a single
        detector and an arbitrary list of TDI P-strings.
    ``TDIFlyGB``
        Single-detector GB response generator (``TDIFly`` + GB waveform,
        F-statistics, likelihood and maximum-likelihood helpers).
    ``TDIFlyGBNetwork``
        Network version of ``TDIFlyGB`` handling several detectors at once.

Usage
-----
Either import the package explicitly::

    from Triangle_GB import TDIFly, TDIFlyGB, TDIFlyGBNetwork

or, as in the examples of this repository::

    from Triangle_GB.TDIFly import *

Requires ``Triangle`` (Triangle-Simulator) to be installed in the same
environment.
"""

__all__ = ["TDIFly", "TDIFlyGB", "TDIFlyGBNetwork"]

from .TDIFly import TDIFly, TDIFlyGB, TDIFlyGBNetwork  # noqa: E402
