# PyTech_update
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

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Jedi"}})
luke = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("  Student ID: " + luke["student_id"] + "\n  First Name: " + luke["first_name"] + "\n  Last Name: " + luke["last_name"] + "\n")

input("\n\n  End of program, press any key to continue...")