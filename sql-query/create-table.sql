-- create table students in clickhouse
CREATE TABLE school_db.students (
    student_id String,
    name String,
    gender String,
    age UInt8,
    school_id String,
    score UInt8
)
ENGINE = MergeTree()
ORDER BY student_id;


--create table schools
CREATE TABLE school_db.schools (
    school_id String,
    school_name String,
    city String
)
ENGINE = MergeTree()
ORDER BY school_id;


-- create table teachers
CREATE TABLE school_db.teachers (
    teacher_id String,
    name String,
    subject String,
    school_id String
)
ENGINE = MergeTree()
ORDER BY teacher_id;