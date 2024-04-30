#!/usr/bin/env python3
"""Write a python function that lists all documents in a collection
Requirement:
    Prototype: def list_all(mongo_collection):
    Return an empty list if no document in collection
    mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    return mongo_collection.find()
