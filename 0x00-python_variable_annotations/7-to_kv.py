#!/usr/bin/env python3
"""Turns a union to a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert an int or float union to a tuple
    """
    return (k, float(v ** 2))
