import pandas as pd
import random

# Load raw data
students = pd.read_csv("./../data/raw/students.csv")
print(f"Original data: {len(students)} rows")


# ----------------------------
# 1. Duplicate records
# ----------------------------
duplicates = students.sample(20, random_state=42)
students = pd.concat([students, duplicates], ignore_index=True)
print("✅ Duplicate records added")


# ----------------------------
# 2. Missing values
# ----------------------------
students.loc[random.sample(range(len(students)), 10), "name"] = None
print("✅ Missing values added")


# ----------------------------
# 3. Invalid age
# ----------------------------
students.loc[random.sample(range(len(students)), 5),
             "age"] = 5  # terlalu kecil
print("✅ Invalid age added")


# ----------------------------
# 4. Invalid foreign key
# ----------------------------
students.loc[random.sample(range(len(students)), 5),
             "school_id"] = "INVALID_SCHOOL"
print("✅ Invalid school_id added")


# ----------------------------
# Save dirty data
# ----------------------------
students.to_csv("./../data/raw/students_dirty.csv", index=False)

print(f"Final dirty data: {len(students)} rows")
print("🔥 Data simulation complete!")
