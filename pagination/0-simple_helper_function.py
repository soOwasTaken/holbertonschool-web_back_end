#!/usr/bin/env python3
"""
simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    simple_helper_function
    """
    return ((page - 1) * page_size, page * page_size)