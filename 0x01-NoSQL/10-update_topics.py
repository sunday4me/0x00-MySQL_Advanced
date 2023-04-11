#!/usr/bin/env python3
"""
Module - update_topics
"""


def update_topics(mongo_collection, name, topics):
    """updaten document in collection"""
    collection = mongo_collection.update_many({"name": name},
                                             {"$set": {"topics": topics}})
