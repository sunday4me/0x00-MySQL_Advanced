#!/usr/bin/env python3
"""
Module - school_by_topics
"""


def schools_by_topic(mongo_collection, topic):
    """find document in collection"""
    collection = mongo_collection.find({"topics": topic})
    return collection
