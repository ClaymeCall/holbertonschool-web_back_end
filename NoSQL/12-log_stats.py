#!/usr/bin/env python3
"""A module that contains a 'nginx_log_stats' function """


from pymongo import MongoClient


def nginx_log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client.logs
        collection = db.nginx

        log_count = collection.count_documents({})
        print(f"{log_count} logs")

        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            count = collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_check_count} status check")

if __name__ == "__main__":
    nginx_log_stats()
