#!/usr/bin/env python3

"""
8-all: Find entries in a collection using pymongo
"""


def list_all(mongo_collection):
    """
    Returns all documents in a collection

    Args:
    mongo_collection (collection): database

    Returns:
    list[]: entries in a collection
    """
    return [d for d in mongo_collection.find()]
