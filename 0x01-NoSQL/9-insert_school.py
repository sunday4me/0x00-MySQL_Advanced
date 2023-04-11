#!/usr/bin/env python3
"""
Module - insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """inserts new document to a collection"""
    collection = mongo_collection.insert_one(kwargs)
    return collection.inserted_id
