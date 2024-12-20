#!/usr/bin/env python3
"""insert_school"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    item = mongo_collection.insert_one(kwargs)
    return item.inserted_id
