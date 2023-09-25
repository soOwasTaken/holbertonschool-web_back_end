#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield a random number between 0 and 10 every second for 10 seconds"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
