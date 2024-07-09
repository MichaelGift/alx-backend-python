#!/usr/bin/env python3
"""Generate a 10 number list using an asynchronous generator
"""
from importlib import import_module as using
from typing import List

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Create a list of 10 numbers from a 10-number generator.
    """
    return [num async for num in async_generator()]
