"""
Exceptions which can be raised by py-Ultroid Itself.
"""


class pyUltroidError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...
