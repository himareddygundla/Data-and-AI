from pymongo import MongoClient
import pandas as pd

# -----------------------------
# CONNECT TO MONGODB
# -----------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]   # Changed database name

# Drop old data (optional for fresh run)
db.students.drop()
db.courses.drop()
db.departments.drop()
db.faculty.drop()
db.registrations.drop()

print("Connected to MongoDB & Database Created\n")

# -----------------------------
# INSERT DOCUMENTS
# -----------------------------

# Departments
departments = [
    {"dept_code": "DEP01", "dept_name": "Software Engineering", "building": "Alpha Block"},
    {"dept_code": "DEP02", "dept_name": "Cyber Security", "building": "Beta Block"},
    {"dept_code": "DEP03", "dept_name": "Data Science", "building": "Gamma Block"},
    {"dept_code": "DEP04", "dept_name": "Robotics", "building": "Delta Block"},
    {"dept_code": "DEP05", "dept_name": "Cloud Computing", "building": "Epsilon Block"}
]
db.departments.insert_many(departments)

# Faculty (renamed from instructors)
faculty = [
    {"faculty_code": "F01", "name": "Dr. Williams", "experience": 9},
    {"faculty_code": "F02", "name": "Prof. Johnson", "experience": 7},
    {"faculty_code": "F03", "name": "Dr. Brown", "experience": 11},
    {"faculty_code": "F04", "name": "Prof. Taylor", "experience": 5},
    {"faculty_code": "F05", "name": "Dr. Anderson", "experience": 14}
]
db.faculty.insert_many(faculty)

# Students
students = [
    {"student_code": "STU01", "name": "Rahul Kumar", "age": 22, "email": "rahul@college.com", "dept_code": "DEP01"},
    {"student_code": "STU02", "name": "Anjali Mehta", "age": 18, "email": "anjali@college.com", "dept_code": "DEP02"},
    {"student_code": "STU03", "name": "Vikram Rao", "age": 24, "email": "vikram@college.com", "dept_code": "DEP03"},
    {"student_code": "STU04", "name": "Sneha Patel", "age": 21, "email": "sneha@college.com", "dept_code": "DEP04"},
    {"student_code": "STU05", "name": "Arjun Singh", "age": 20, "email": "arjun@college.com", "dept_code": "DEP05"}
]
db.students.insert_many(students)

# Courses
courses = [
    {"course_code": "COUR01", "course_title": "Full Stack Development", "credits": 4, "faculty_code": "F01"},
    {"course_code": "COUR02", "course_title": "Ethical Hacking", "credits": 3, "faculty_code": "F02"},
    {"course_code": "COUR03", "course_title": "Big Data Analytics", "credits": 4, "faculty_code": "F03"},
    {"course_code": "COUR04", "course_title": "Automation Systems", "credits": 2, "faculty_code": "F04"},
    {"course_code": "COUR05", "course_title": "AWS Fundamentals", "credits": 3, "faculty_code": "F05"}
]
db.courses.insert_many(courses)

# Registrations (renamed from enrollments)
registrations = [
    {"student_code": "STU01", "course_code": "COUR01"},
    {"student_code": "STU02", "course_code": "COUR02"},
    {"student_code": "STU03", "course_code": "COUR03"},
    {"student_code": "STU04", "course_code": "COUR01"},
    {"student_code": "STU05", "course_code": "COUR04"}
]
db.registrations.insert_many(registrations)

print("Data Inserted Successfully\n")

# -----------------------------
# READ OPERATIONS
# -----------------------------

print("All Students:")
for s in db.students.find():
    print(s)

print("\nStudents older than 20:")
for s in db.students.find({"age": {"$gt": 20}}):
    print(s)

# -----------------------------
# UPDATE OPERATION
# -----------------------------
db.students.update_one(
    {"student_code": "STU01"},
    {"$set": {"email": "rahul_updated@college.com"}}
)
print("\nUpdated Email for STU01")

# -----------------------------
# DELETE OPERATION
# -----------------------------
db.students.delete_one({"student_code": "STU05"})
print("Deleted Student STU05\n")

# -----------------------------
# CREATE INDEX
# -----------------------------
db.students.create_index("email")
print("Index Created on Email\n")

# -----------------------------
# AGGREGATION
# -----------------------------
print("Students Per Department:")
result = db.students.aggregate([
    {"$group": {"_id": "$dept_code", "total": {"$sum": 1}}}
])
for r in result:
    print(r)

# -----------------------------
# EXPORT TO CSV
# -----------------------------

def export_to_csv(collection_name):
    data = list(db[collection_name].find())
    if data:
        df = pd.DataFrame(data)
        df.drop(columns=["_id"], inplace=True)
        df.to_csv(f"{collection_name}.csv", index=False)
        print(f"{collection_name}.csv exported successfully")

export_to_csv("students")
export_to_csv("courses")
export_to_csv("departments")
export_to_csv("faculty")
export_to_csv("registrations")

print("\nAll CSV files created successfully!")