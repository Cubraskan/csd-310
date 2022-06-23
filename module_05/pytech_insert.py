from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ihluj.mongodb.net/pytech"
client=MongoClient(url)
db=client.pytech

andrew = {
    "student_id": "1007",
    "first_name": "Andrew",
    "last_name": "Cano"
}

karen = {
    "student_id": "1008",
    "first_name": "Karen",
    "last_name": "Hall"
}

tim = {
    "student_id": "1009",
    "first_name": "Tim",
    "last_name": "Lentz"
}

students = db.students

print("\n -- INSERT STATEMENTS --")
andrew_student_id = students.insert_one(andrew).inserted_id
print(" Inserted student record Andrew Cano into the students collection with document_id " + str(andrew_student_id))

karen_student_id = students.insert_one(karen).inserted_id
print(" Inserted student record Karen Hall into the students collection with document_id " + str(karen_student_id))

tim_student_id = students.insert_one(tim).inserted_id
print(" Inserted student record Tim Lentz into the students collection with document_id " + str(tim_student_id))

input("\n End of program, please press enter to exit...")