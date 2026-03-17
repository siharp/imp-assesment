import pandas as pd
import random
from faker import Faker

fake = Faker("id_ID")


# generate prefix
def generate_id(prefix, num):
    return f"{prefix}-{str(num).zfill(3)}"


# count data
NUM_SCHOOLS = 50
NUM_STUDENTS = 1000
NUM_TEACHERS = 200


# ------------------
# Schools
# ------------------
schools = []
for i in range(NUM_SCHOOLS):
    schools.append({
        "school_id": generate_id("SCH", i+1),
        "school_name": f"SMA {fake.city()}",
        "city": fake.city()
    })
schools = pd.DataFrame(schools)
school_ids = schools["school_id"].tolist()


# ------------------
# Teachers
# ------------------
subjects = [
    "Matematika", "Fisika", "Kimia",
    "Biologi", "Bahasa Inggris",
    "Sejarah", "Ekonomi", "Geografi"
]
teachers = []
for i in range(NUM_TEACHERS):
    teachers.append({
        "teacher_id": generate_id("TCH", i+1),
        "name": fake.name(),
        "subject": random.choice(subjects),
        "school_id": random.choice(school_ids)
    })
teachers = pd.DataFrame(teachers)


# ------------------
# Students
# ------------------
students = []
for i in range(NUM_STUDENTS):
    students.append({
        "student_id": generate_id("STD", i+1),
        "name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(15, 18),
        "school_id": random.choice(school_ids),
        "score": random.randint(40, 100)
    })
students = pd.DataFrame(students)


# saved data to csv file
schools.to_csv("./../data/raw/schools.csv", index=False)
teachers.to_csv("./../data/raw/teachers.csv", index=False)
students.to_csv("./../data/raw/students.csv", index=False)
