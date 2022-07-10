from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jscwh.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collections_names)

input("\n\n End of program, press any key to exit... ")