#!/usr/bin/env python3
"""This index_range function takes two integer arguments page and page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The return of tuple of size two containing a start index
    and an end index"""
    end_page = page * page_size
    start_page = end_page - page_size
    return(start_page, end_page)
