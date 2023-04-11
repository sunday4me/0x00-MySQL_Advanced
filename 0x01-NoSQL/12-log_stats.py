#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    count_logs = collection.count_documents({})
    print("{} logs".format(count_logs))
 
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    count_status = collection.count_documents({"path": "/status"})
    print("{} status check".format(count_status))
