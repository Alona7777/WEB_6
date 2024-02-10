 --1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    SELECT 
        s.id, 
        s.fullname, 
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;

    -- 2. Знайти студента із найвищим середнім балом з певного предмета.
    SELECT 
        s.id, 
        s.fullname, 
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    WHERE g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;

    -- 3. Знайти середній бал у групах з певного предмета.
    SELECT g.name AS group_name,
        ROUND(AVG(grade), 2) AS average_grade
    FROM grades gr
    JOIN students s ON gr.student_id = s.id
    JOIN groups g ON s.group_id = g.id
    JOIN subjects subj ON gr.subject_id = subj.id
    WHERE subj.id = 3
    GROUP BY g.name;
  
    -- 4. Знайти середній бал на потоці (по всій таблиці оцінок).
    SELECT 
    ROUND(AVG(grade), 2) AS average_grade
    FROM grades;
    
    -- 5. Знайти які курси читає певний викладач.
    SELECT
        s.id,
        s.name
    FROM subjects s
    JOIN teachers t ON t.id = s.teacher_id
    where s.teacher_id = 1
    GROUP BY s.name;
  
    -- 6. Знайти список студентів у певній групі.
    SELECT
        s.id,
        s.fullname
    FROM students s
    JOIN groups g ON g.id = s.group_id
    WHERE g.id = 2
    GROUP BY s.id;

    --7. Знайти оцінки студентів у окремій групі з певного предмета.
    SELECT
        s.fullname,
        gr.grade
    FROM grades gr
    JOIN students s ON gr.student_id = s.id
    JOIN groups g ON s.group_id = g.id
    JOIN subjects subj ON gr.subject_id = subj.id
    WHERE g.id = 3 AND subj.id = 3
    ORDER BY gr.grade DESC;

    -- 8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
    SELECT
        ROUND(AVG(grade), 2) AS average_grade
    FROM grades gr
    JOIN subjects subj ON gr.subject_id = subj.id
    JOIN teachers t ON subj.teacher_id = t.id
    WHERE t.id = 1;
   
    -- 9. Знайти список курсів, які відвідує студент.
    SELECT DISTINCT 
        subj.name AS subject_name
    FROM students s
    JOIN grades gr ON s.id = gr.student_id
    JOIN subjects subj ON gr.subject_id = subj.id
    WHERE s.id = 7;
   
    -- 10. Список курсів, які певному студенту читає певний викладач.
    SELECT DISTINCT 
        subj.name AS subject_name
    FROM students s
    JOIN grades gr ON s.id = gr.student_id
    JOIN subjects subj ON gr.subject_id = subj.id
    JOIN teachers t ON subj.teacher_id = t.id
    WHERE s.id = 7 AND t.id = 1;

    -- 11. Середній бал, який певний викладач ставить певному студентові.
    SELECT
        ROUND(AVG(grade), 2) AS average_grade
    FROM students s
    JOIN grades gr ON s.id = gr.student_id
    JOIN subjects subj ON gr.subject_id = subj.id
    JOIN teachers t ON subj.teacher_id = t.id
    WHERE s.id = 7 AND t.id = 1;

    -- 12.Оцінки студентів у певній групі з певного предмета на останньому занятті.
    SELECT
        s.fullname,
        gr.grade
    FROM grades gr
    JOIN students s ON gr.student_id = s.id
    JOIN groups g ON s.group_id = g.id
    JOIN subjects subj ON gr.subject_id = subj.id
    WHERE g.id = 1
      AND subj.id = 3
      AND gr.grade_date = (
    SELECT MAX(grade_date)
    FROM grades
    WHERE subject_id = subj.id
  );
 