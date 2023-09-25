#!/usr/bin/env python3
"""Basic annotations"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each tuple containing a string"""
    return [(i, len(i)) for i in lst]
