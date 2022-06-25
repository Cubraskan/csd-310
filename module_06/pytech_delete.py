from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ihluj.mongodb.net/pytech"
client=MongoClient(url)
db=client.pytech
students = db.students

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
find_students = students.find({})
for doc in find_students:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

julie = {
    "student_id": "1010",
    "first_name": "Julie",
    "last_name": "Rogers",
}

print("\n--INSERT STATEMENTS--")
julie_student_id = students.insert_one(julie).inserted_id
print(" Inserted student record Julie Rogers into the students collection with document_id " + str(julie_student_id) + "\n")

new = students.find_one({"student_id":"1010"})
print("--DISPLAYING STUDENT TEST DOC--")
print(" Student ID: " + new["student_id"] + "\n First Name: " + new["first_name"] + "\n Last Name: " + new["last_name"] + "\n")

students.delete_one({"student_id": "1010"})

print("\n--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")
find_students = students.find({})
for doc in find_students:
    print("Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")