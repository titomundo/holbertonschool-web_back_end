#!/usr/bin/env python3

"""
9-insert_school: Insert data into collection using pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection

    Args:
    mongo_collection (collection): Collection to insert into
    kwargs (dict): data to create the new record
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
