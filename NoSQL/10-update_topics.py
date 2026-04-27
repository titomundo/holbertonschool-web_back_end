#!/usr/bin/env python3

"""
10-update_topics: Update documents in a collection using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    Update documents matching a value

    Args:
    mongo_collection (collection): Collection to insert into
    name (str): name of the school to update
    topics (list): data to update
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
