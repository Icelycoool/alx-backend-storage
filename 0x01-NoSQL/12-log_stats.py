#!/usr/bin/env python3
"""stats"""

from pymongo import MongoClient


def stats_log():
    """Displays some stats abount Nginx logs stored in MongoDB"""
    # Connect to the client
    client = MongoClient('mongodb://localhost:27017')

    # Access the logs
    log_collection = client.logs.nginx

    # Get the total number of logs
    total_logs = log_collection.count_documents({})

    # Count the logs of each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: log_collection.count_documents({
            "method": method}) for method in methods
    }

    # Status count for GET method
    get_status_count = log_collection.count_documents({
        "method": "GET", "path": "/status"
    })

    # Display information
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{get_status_count} status check")


if __name__ == "__main__":
    stats_log()
