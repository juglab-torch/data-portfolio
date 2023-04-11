"""data_protfolio.

A helper package to download example datasets used in various publications
by the Jug lab, including data featured in N2V, P(P)N2V, DivNoising, HDN,
EmbedSeg, etc.
"""
__all__ = ["Portfolio", "__author__", "__email__", "__version__"]

from importlib.metadata import PackageNotFoundError, version

from .portfolio import Portfolio

try:
    __version__ = version("data-portfolio")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Joran Deschamps"
__email__ = "joran.deschamps@fht.org"
