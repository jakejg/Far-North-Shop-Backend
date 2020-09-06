from pymongo import MongoClient

client = MongoClient()

db = client.far_north

items = db.items