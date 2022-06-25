from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ihluj.mongodb.net/pytech"
client=MongoClient(url)
db=client.pytech
students = db.students

student_list = students.find({})

print("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in student_list:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

update = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Ryan"}})

andrew = students.find_one({"student_id": "1007"})

print("\n -- DISPLAYING UPDATED STUDENT DOCUMENT 1007 --")

print(" Student ID: " + andrew["student_id"] + "\n First Name: " + andrew["first_name"] + "\n Last Name: " + andrew["last_name"] + "\n")

input("\n End of program, press any key to continue...")