#!/usr/bin/env python3
"""This index_range function takes two integer arguments page and page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The return of tuple of size two containing a start index
    and an end index"""
    temp1 = page * page_size
    temp2 = temp1 - page_size
    return(temp2, temp1)
