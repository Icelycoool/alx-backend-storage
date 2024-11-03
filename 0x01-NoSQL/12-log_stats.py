#!/usr/bin/env python3
"""stats"""

from pymongo import MongoClient

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def stats_log(log_collection):
    """Displays some stats about Nginx logs stored in MongoDB"""

    # Get the total number of logs
    total_logs = log_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")

    # Initialize a dictionary to store counts for each method
    method_counts = {method: 0 for method in methods}

    # Count the logs of each method
    for method in methods:
        method_counts[method] = log_collection.count_documents(
            {"method": method}
        )

    # Status count for GET method
    get_status_count = log_collection.count_documents({
        "method": "GET", "path": "/status"
    })

    # Print the counts for each method
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    print(f"{get_status_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    stats_log(log_collection)
