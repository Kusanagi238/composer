# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Some key classes are available directly in the ``composer`` namespace."""

from composer._version import __version__
from composer.core import (
    Algorithm,
    Callback,
    DataSpec,
    Engine,
    Evaluator,
    Event,
    State,
    Time,
    Timestamp,
    TimeUnit,
)
from composer.loggers import Logger
from composer.models import ComposerModel


# Delay importing heavy submodules (like composer.trainer) until attribute access to avoid
# pulling optional dependencies (e.g., transformers) at package import time.
def __getattr__(name):
    if name == "Trainer":
        from composer.trainer import Trainer as _Trainer

        globals()["Trainer"] = _Trainer
        return _Trainer
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Algorithm",
    "Callback",
    "DataSpec",
    "Engine",
    "Evaluator",
    "Event",
    "State",
    "Time",
    "Timestamp",
    "TimeUnit",
    "Logger",
    "ComposerModel",
    "Trainer",
]
