#!/usr/bin/env python3
"""A module that contains a 'update_topics' function """


def update_topics(mongo_collection, name, topics):
    """ Updates the contents of a school based on name """
    if mongo_collection is None:
        return None

    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
