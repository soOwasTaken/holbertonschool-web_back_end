#!/usr/bin/env python3
"""Basic annotations - async"""
import asyncio
import random
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay"""
    tasks = [asyncio.create_task(wait_random.wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
