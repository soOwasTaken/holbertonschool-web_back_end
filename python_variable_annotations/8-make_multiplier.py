#!/usr/bin/env python3
"""Basic annotations - make multiplier"""
from typing import Callable  # Import Callable from the typing module


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its input by the multiplier."""
    def f(n: float) -> float:
        return n * multiplier
    return f
