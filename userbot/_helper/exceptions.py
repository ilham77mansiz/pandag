"""
Exceptions which can be raised by py-Ultroid Itself.
"""


class PandaUserbotError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(PandaUserbotError):
    ...
