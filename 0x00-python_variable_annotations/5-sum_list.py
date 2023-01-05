#!/usr/bin/env python3
from typing import List
"""5-sum_list"""


def sum_list(input_list: List[float]) -> float:
    """returns the sum of a list of floats"""
    result: float = 0.0
    for num in input_list:
        result += num
    return result