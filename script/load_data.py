from sqlalchemy import create_engine
import pandas as pd

# create engine for mysql
engine = create_engine(
    "mysql+pymysql://school_user:school_password@localhost:3306/school_db")

# read data
schools = pd.read_csv("./../data/raw/schools.csv")
teachers = pd.read_csv("./../data/raw/teachers.csv")
students = pd.read_csv("./../data/raw/students.csv")


# load data to mysql
students.to_sql(
    "students",
    engine,
    if_exists="replace",
    index=False
)

teachers.to_sql(
    "teachers",
    engine,
    if_exists="replace",
    index=False
)

schools.to_sql(
    "schools",
    engine,
    if_exists="replace",
    index=False
)
