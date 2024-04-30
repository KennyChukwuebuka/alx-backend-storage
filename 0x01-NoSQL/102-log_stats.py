#!/usr/bin/env python3
"""Improve your previous log_stats.py script by adding
"""

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient()
db = client['logs']
collection = db['nginx']

# Get the total number of documents
total_docs = collection.count_documents({})

# Get the count of documents by method
methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
method_counts = [collection.count_documents({'method':
                                             method}) for method in methods]

# Get the count of documents with method=GET and path=/status
status_checks = collection.count_documents({'method': 'GET',
                                            'path': '/status'})

# Get the top 10 IPs
ips = collection.aggregate([
    {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}},
    {'$limit': 10}
])

# Print the results
print(f'{total_docs} logs')
print('Methods:')
for method, count in zip(methods, method_counts):
    print(f'\tmethod {method}: {count}')
print(f'{status_checks} status check')
print('IPs:')
for ip in ips:
    print(f'{ip["_id"]}: {ip["count"]}')
