#!/usr/bin/env python3
""" This module contains a 'index_range' function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns the page range base on current and scope size """
    first_elem_of_page = page_size * (page - 1)
    last_elem_of_page = first_elem_of_page + page_size

    return (first_elem_of_page, last_elem_of_page)
