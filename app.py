from flask import Flask, request, jsonify
from dbSetup import items
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from flask_cors import CORS
from models import Item

app = Flask(__name__)


CORS(app)

@app.route('/items')
def get_all_items():
    """Route to get all items"""

    allItems = list(items.find())
    for item in allItems:
        # convert ObjectId from MongoDb to string
        id_to_string(item)
    
    return jsonify(allItems)

@app.route('/items/<id>')
def get_item(id):
    """Route to get item by id"""

    item = items.find_one({'_id': ObjectId(id)})

    # convert ObjectId from MongoDb to string
    id_to_string(item)
    
    return item

@app.route('/items', methods=['POST'])
def create_item():
    """Route to create an item"""
  
    data = request.get_json()

    item = Item(
        description = data.get('description'),
        price = data.get('price'),
        type = data.get('type'),
        img = data.get('img'),
        quantity = data.get('quantity'),
        name = data.get('name')
        )

    # get image name
    name = item.get_img_name()

    # save image on server
    base64Image = data.get('imgFile')
    Item.save_img(base64Image, name)
    
    #save item in db
    result = items.insert_one(item.__dict__)
    item = items.find_one({'_id': result.inserted_id})
    id_to_string(item)
    return item

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    """Route to delete an item by id"""

    items.delete_one({'_id': ObjectId(id)})

    return "Success"

@app.route('/items/<id>', methods=['PATCH'])
def update_item(id):
    """Route to update an item"""

    data = request.get_json()

    item = items.find_one_and_update({'_id': ObjectId(id)}, {'$set': data}, return_document=ReturnDocument.AFTER)

    # convert ObjectId from MongoDb to string
    id_to_string(item)
    
    return item


def id_to_string(item):
    item['_id'] = str(item['_id'])
