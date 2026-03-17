-- Total Students by School
SELECT
  s.school_name,
  COUNT(st.student_id) total_students
FROM students st
JOIN schools s
  ON st.school_id = s.school_id
GROUP BY s.school_name
ORDER BY total_students DESC;


-- Average Score by School
SELECT
  s.school_name,
  AVG(st.score) avg_score
FROM students st
JOIN schools s
  ON st.school_id = s.school_id
GROUP BY s.school_name;


-- Student-Teacher Ratio (STR)
SELECT
  s.school_name,
  COUNT(DISTINCT t.teacher_id) teachers,
  COUNT(DISTINCT st.student_id) students
FROM schools s
LEFT JOIN teachers t
  ON s.school_id = t.school_id
LEFT JOIN students st
  ON s.school_id = st.school_id
GROUP BY s.school_name;


-- Gender Distribution
SELECT
  gender,
  COUNT(*) total
FROM students
GROUP BY gender;


-- age Distribution
SELECT
  age,
  COUNT(*) total
FROM students
GROUP BY gender;


-- Top 10 High-Achieving Students
SELECT
  name,
  score,
FROM students
ORDER BY score DESC
LIMIT 10;


-- Top 10 School high students score
SELECT
  name,
  score,
  scl.school_name
FROM students std
JOIN School scl
  ON std.school_id = scl.school_id
ORDER BY score DESC
LIMIT 10;