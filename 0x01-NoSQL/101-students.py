#!/usr/bin/env python3
"""
Module - 101-students
"""


def top_students(mongo_collection):
    """
    Use the aggregation framework to calculate
    the average score for each student
    """
    pipeline = [
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipeline)
