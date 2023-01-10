#!/usr/bin/env python3
"""2-measure_runtime.py"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Asynchronous coroutine that returns the execution time """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.time() - start
