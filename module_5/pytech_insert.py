from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

jane = {
    "student_id": "1007",
    "first_name": "Jane",
    "last_name": "Doe",
}

john = {
    "student_id": "1008",
    "first_name": "John",
    "last_name": "Doe",
}

johnny = {
    "student_id": "1009",
    "first_name": "Johnny",
    "last_name": "Test",
}

students = db.students

print("\n  -- INSERT STATEMENTS --")
jane_student_id = students.insert_one(jane).inserted_id
print("  Inserted student record Jane Doe into the students collection with document_id " + str(jane_student_id))

john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Doe into the students collection with document_id " + str(john_student_id))

johnny_student_id = students.insert_one(johnny).inserted_id
print("  Inserted student record Johnny Test into the students collection with document_id " + str(johnny_student_id))

input("\n\n  End of program, press any key to exit... ")