from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ihluj.mongodb.net/pytech"
client=MongoClient(url)
db=client.pytech
students=db.students

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")

list_students = students.find({})

for doc in list_students:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")

andrew = students.find_one({"student_id": "1007"})

print(" Student ID: " + andrew["student_id"] + "\n First Name: " + andrew["first_name"] + "\n Last Name: " + andrew["last_name"] + "\n")

input("\n End of program, press any key to continue...")