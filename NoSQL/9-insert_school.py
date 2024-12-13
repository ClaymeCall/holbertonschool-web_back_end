#!/usr/bin/env python3
"""A module that contains a 'insert_school' function """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection"""
    if mongo_collection is None:
        return None

    return mongo_collection.insert_one(kwargs).inserted_id
