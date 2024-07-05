#!/usr/bin/env python3
"""This module contains a function that adds all numbers in a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Get sum of all numbers in a float list
    """
    return float(sum(input_list))
