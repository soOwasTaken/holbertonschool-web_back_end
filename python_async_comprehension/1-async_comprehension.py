#!/usr/bin/env python3
"""Async Generator"""""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """get 10 rand numbers using an async comprehensing over async_generator"""
    return [number async for number in async_generator()]
