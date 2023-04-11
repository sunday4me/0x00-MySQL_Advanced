#!/usr/bin/env python3
"""
Module - all
"""


def list_all(mongo_collection):
    """lists all documents collection"""
    collection = list(mongo_collection.find({}))
    return collection
