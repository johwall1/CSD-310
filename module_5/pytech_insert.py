from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jscwh.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

luke = {
    "student_id": "1007",
    "first_name": "Luke",
    "last_name": "Skywalker",
}

darth = {
    "student_id": "1008",
    "first_name": "Darth",
    "last_name": "Vader",
}

ahsoka = {
    "student_id": "1009",
    "first_name": "Ahsoka",
    "last_name": "Tano",
}

students = db.students

print("\n  -- INSERT STATEMENTS --")
luke_student_id = students.insert_one(luke).inserted_id
print("  Inserted student record Jane Doe into the students collection with document_id " + str(luke_student_id))

darth_student_id = students.insert_one(darth).inserted_id
print("  Inserted student record John Doe into the students collection with document_id " + str(darth_student_id))

ahsoka_student_id = students.insert_one(ahsoka).inserted_id
print("  Inserted student record Johnny Test into the students collection with document_id " + str(ahsoka_student_id))

input("\n\n  End of program, press any key to exit... ")