#!/usr/bin/env python3
"""A module that contains a 'nginx_log_stats' function """

from pymongo import MongoClient


def nginx_stats():
    """Function that provides Stats about Nginx logs stored in MongoDB"""

    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    nginx_collection = db.nginx

    n_logs = nginx_collection.count_documents({})
    print(f"{n_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )

    print(f"{status_check} status check")

if __name__ == "__main__":
    nginx_stats()
