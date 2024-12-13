#!/usr/bin/env python3
"""A module that contains a 'schools_by_topic' function """


def schools_by_topic(mongo_collection, topic):
    """Returns all schools matching a topic"""
    if mongo_collection is None:
        return []

    return mongo_collection.find({"topics": topic})
