#!/usr/bin/env python3
""" This module contains a 'index_range' function """

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns the page range based on current and scope size """
    first_elem_of_page = page_size * (page - 1)
    last_elem_of_page = first_elem_of_page + page_size

    return (first_elem_of_page, last_elem_of_page)


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
        """Gets the contents corresponding to a certain page in the dataset"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dict containing the data dataset targeted
        by the pagination range
        """
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        data = self.get_page(page, page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
