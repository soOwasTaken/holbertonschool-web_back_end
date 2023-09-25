#!/usr/bin/env python3
"""Basic annotations - to_kv"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple"""
    return (k, v * v)

