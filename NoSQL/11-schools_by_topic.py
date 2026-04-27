#!/usr/bin/env python3

"""
11-schools_by_topic: Filter by values using pymongo
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns all documents in a collection matching a value

    Args:
    mongo_collection (collection): database

    Returns:
    list[]: entries in a collection
    """
    return [d for d in mongo_collection.find({"topic": topic})]
