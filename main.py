from students_query import execute_query


# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql_1 = """
SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;
"""

# 2. Знайти студента із найвищим середнім балом з певного предмета.
sql_2 = """
SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
WHERE g.subject_id = 5
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
"""

# 3. Знайти середній бал у групах з певного предмета.
sql_3 = """
SELECT g.name AS group_name,
    ROUND(AVG(grade), 2) AS average_grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE subj.id = 3
GROUP BY g.name;
"""

# 4. Знайти середній бал на потоці (по всій таблиці оцінок).
sql_4 = """
SELECT 
ROUND(AVG(grade), 2) AS average_grade
FROM grades;
"""

# 5. Знайти які курси читає певний викладач.
sql_5 = """
SELECT
    s.id,
    s.name
FROM subjects s
JOIN teachers t ON t.id = s.teacher_id
where s.teacher_id = 4
GROUP BY s.name;
"""

# 6. Знайти список студентів у певній групі.
sql_6 = """
SELECT
    s.id,
    s.fullname
FROM students s
JOIN groups g ON g.id = s.group_id
WHERE g.id = 2
GROUP BY s.id;
"""

# 7. Знайти оцінки студентів у окремій групі з певного предмета.
sql_7 = """
SELECT
    s.fullname,
    gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE g.id = 3 AND subj.id = 7
ORDER BY gr.grade DESC;
"""

# 8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
sql_8 = """
SELECT
    ROUND(AVG(grade), 2) AS average_grade
FROM grades gr
JOIN subjects subj ON gr.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
WHERE t.id = 5;
"""

# 9. Знайти список курсів, які відвідує студент.
sql_9 = """
SELECT DISTINCT 
    subj.name AS subject_name
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE s.id = 7;
"""

# 10. Список курсів, які певному студенту читає певний викладач.
sql_10 = """
SELECT DISTINCT 
    subj.name AS subject_name
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN subjects subj ON gr.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
WHERE s.id = 30 AND t.id = 3;
"""

# 11. Середній бал, який певний викладач ставить певному студентові.
sql_11 = """
SELECT
    ROUND(AVG(grade), 2) AS average_grade
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN subjects subj ON gr.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
WHERE s.id = 7 AND t.id = 4;
"""

# 12.Оцінки студентів у певній групі з певного предмета на останньому занятті.
sql_12 = """
SELECT
    s.fullname,
    gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE g.id = 1
    AND subj.id = 7
    AND gr.grade_date = (
SELECT MAX(grade_date)
FROM grades
WHERE subject_id = subj.id
);
"""

if __name__ == "__main__":
  
    
    print(execute_query(sql_1))  
    print(execute_query(sql_2)) 
    print(execute_query(sql_3))
    print(execute_query(sql_4)) 
    print(execute_query(sql_5)) 
    print(execute_query(sql_6)) 
    print(execute_query(sql_7))  
    print(execute_query(sql_8))  
    print(execute_query(sql_9))  
    print(execute_query(sql_10)) 
    print(execute_query(sql_11))  
    print(execute_query(sql_12))  
