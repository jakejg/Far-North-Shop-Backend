from dbSetup import db

sample_data = [
    {
      "description": "Alaskan Birch Wood Bowl",
      "price": 75,
      "type": "Bowl",
      "img": 'AKBowl.jpg'
    },
    {
      "description": "End grain cutting board",
      "price": 135,
      "type": 'board',
      "img" : 'EndGrainBoard.jpg'
    },
    {
      "description": "Alaskan Birch Wood Bowl",
      "price": 75,
      "type": "Bowl",
      "img": 'AKBowl.jpg'
    },
    {
      "description": "End grain cutting board",
      "price": 135,
      "type": 'board',
      "img" : 'EndGrainBoard.jpg'
    }
]

db.items.drop()
items = db['items']

items.insert_many(sample_data)
