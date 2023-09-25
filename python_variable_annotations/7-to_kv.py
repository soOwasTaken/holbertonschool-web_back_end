#!/usr/bin/env python3
"""Basic annotations - to_kv"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a tuple"""
    return (k, v * v)
