# PyTech_delete
# Module 6
# John Wall
# 07/17/2022

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jscwh.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# New test User
anakin = {
   "student_id": "1010",
    "first_name": "Anakin",
    "last_name": "Skywalker" 
}

print("\n  -- INSERT STATEMENTS --")
anakin_student_id = students.insert_one(anakin).inserted_id
print("  Inserted student record Anakin Skywalker into the students collection with document_id " + str(anakin_student_id))

anakin = students.find_one({"student_id": "1010"})
print("\n  -- DISPLAYING STUDENT TEST DOC --")
print("  Student ID: " + anakin["student_id"] + "\n  First Name: " + anakin["first_name"] + "\n  Last Name: " + anakin["last_name"] + "\n")

deleted_student = students.delete_one({"student_id": "1010"})

student_list = students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")