# #!/usr/bin/env python3
# """stats"""
# from pymongo import MongoClient


# if __name__ == "__main__":
#     """Displays some stats about Nginx logs stored in MongoDB"""
#     client = MongoClient('mongodb://127.0.0.1:27017')
#     log_collection = client.logs.nginx

#     # Get the total number of logs
#     total_logs = log_collection.count_documents({})
#     print(f"{total_logs} logs")

#     # Count the logs of each method
#     methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
#     print("Methods:")
#     for method in methods:
#         count = log_collection.count_documents({"method": method})
#         print(f"\tmethod {method}: {count}")

#     # Status count for GET method
#     get_status_count = log_collection.count_documents(
#         {"method": "GET", "path": "/status"}
#     )

#     print(f"{get_status_count} status check")
#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')