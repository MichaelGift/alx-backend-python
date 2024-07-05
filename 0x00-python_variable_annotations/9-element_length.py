#!/usr/bin/env python3
"""This module contains a function that returns list tuple
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Iterate over alist and return a tuple
    containing the length of the longest sequence
    """
    return [(i, len(i)) for i in lst]
