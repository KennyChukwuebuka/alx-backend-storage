#!/usr/bin/env python3
"""Improve your previous log_stats.py script by adding
"""

from pymongo import MongoClient


def get_log_stats():
    """gets log stats"""
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
        print(f"    method {method}: {count}")

    # Count status check
    count_status_check = collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{count_status_check} status check")

    # Top 10 IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)
    for index, ip in enumerate(top_ips, start=1):
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    get_log_stats()
