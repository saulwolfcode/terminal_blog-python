import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["diseño"]
collection = database["equipo"]

"""
equipo = collection.find({})

for nosotros in equipo:
    print(nosotros)
"""
equipo=[equipo1 for equipo1 in collection.find({})]
print(equipo)