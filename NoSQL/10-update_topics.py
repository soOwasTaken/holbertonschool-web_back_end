#!/usr/bin/env python3
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """ Change all topics of a school document based on the name """
    update_result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return update_result.modified_count