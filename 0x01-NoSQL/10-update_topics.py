#!/usr/bin/env python3
"""update_topics"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on name"""
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )