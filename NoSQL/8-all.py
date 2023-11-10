#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """ List all documents in a collection """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
