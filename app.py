from flask import Flask, request, jsonify
from dbSetup import items

app = Flask(__name__)

@app.route('/items')
def get_all_items():
    """Route to get all items"""

    allItems = list(items.find())
    for item in allItems:
        # convert ObjectId from MongoDb to string
        item['_id'] = str(item['_id'])
    
    return jsonify(allItems)

@app.route('/items', methods=['POST'])
def create_item():
    """Route to create an item"""

    data = request.get_json()
    items.insert_one(data)

    return "Success"
