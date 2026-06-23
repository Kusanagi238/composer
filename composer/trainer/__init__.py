# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Train models with flexible insertion of algorithms."""

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from composer.trainer.trainer import Trainer  # pragma: no cover
else:

    def __getattr__(name: str):
        if name == "Trainer":
            module = importlib.import_module("composer.trainer.trainer")
            return getattr(module, "Trainer")
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    def __dir__():
        return sorted(globals().keys() | {"Trainer"})


__all__ = ["Trainer"]
