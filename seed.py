from dbSetup import db

sample_data = [
    {
      "description": "Alaskan Birch Wood Bowl that is safe for all of you PLANT foods",
      "price": 75,
      "type": "Bowl",
      "img": 'AKBowl.jpg',
      "quantity": 1,
      "name" : "Alaskan Birch Wood Bowl"
    },
    {
      "description": "Most pretty cutting board you'll ever see",
      "price": 135,
      "type": 'board',
      "img" : 'EndGrainBoard.jpg',
      "quantity": 1,
      "name" : "End grain cutting board"
    },
    {
      "description": "Alaskan Birch Wood Bowl that is safe for all of you PLANT foods",
      "price": 75,
      "type": "Bowl",
      "img": 'AKBowl.jpg',
      "quantity": 1,
      "name" : "Alaskan Birch Wood Bowl"
    },
    {
      "description": "Most pretty cutting board you'll ever see",
      "price": 135,
      "type": 'board',
      "img" : 'EndGrainBoard.jpg',
      "quantity": 1,
      "name" : "End grain cutting board"
    }
]

db.items.drop()
items = db['items']

items.insert_many(sample_data)
