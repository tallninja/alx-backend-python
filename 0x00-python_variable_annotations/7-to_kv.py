#!/usr/bin/env python3
"""7-to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        takes a string k and an int OR float v
        as arguments and returns a tuple
    """
    cncat: Tuple(str, Union[int, float])
    cncat = (k, v**2)

    return cncat
