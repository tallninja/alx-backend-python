#!/usr/bin/env python3
"""1-concurrent_coroutines.py"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays: List[float] = []
    for _ in range(n):
        delay: float = await wait_random(max_delay)
        delays.append(delay)
    return delays
