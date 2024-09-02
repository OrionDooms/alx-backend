#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple, Dict


def positive_int(x):
    """This function tests the value if it's positive and if it's integer """
    return isinstance(x, int) and x > 0


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """The return of tuple of size two containing a start index
    and an end index"""
    end_page = page * page_size
    start_page = end_page - page_size
    return(start_page, end_page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """The positive_int test the integer of page and page_size"""
        assert positive_int(page)
        assert positive_int(page_size)

        start_page, end_page = index_range(page, page_size)
        data = self.dataset()
        if len(data) < start_page:
            return []
        return data[start_page:end_page]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        SumOfItems = sum(1 for item in self.dataset())
        total_pages = math.ceil(SumOfItems / page_size)

        return {
                "page_size": len(self.get_page(page, page_size)),
                "page": page,
                "data": (self.get_page(page, page_size)),
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }
