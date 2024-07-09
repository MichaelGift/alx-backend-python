#!/usr/bin/env python3
"""Generate random floats asynchronously
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Return a generator that yields float values.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10