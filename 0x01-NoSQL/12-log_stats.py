#!/usr/bin/env python3
"""Write a Python script that provides some stats
about Nginx logs stored in MongoDB:
"""


from pymongo import MongoClient


def get_log_stats():
    """
    A function that connects to MongoDB, retrieves
    log stats, and prints the total number of
    logs, counts methods such as
    GET, POST, PUT, PATCH, and DELETE, and checks the status.
    """
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status check
    count_status_check = collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{count_status_check} status check")


if __name__ == "__main__":
    get_log_stats()
