#!/usr/bin/env python3
"""Basic annotations - make multiplication"""


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """Return a function"""
    def f(n: float):
        return (n * multiplier)
    return f
