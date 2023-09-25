#!/usr/bin/env python3
"""Basic annotations - async"""
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    start = loop.time()
    loop.run_until_complete(wait_n(n, max_delay))
    end = loop.time()

    return (end - start) / n
