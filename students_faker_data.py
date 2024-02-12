import random
import faker
from random import randint
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 9
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20

def insert_data_to_db() -> None:
    fake = faker.Faker()

    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними
    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        # Додавання груп
        for _ in range(NUMBER_GROUPS):
            cur.execute("INSERT INTO groups (name) VALUES (?)", (fake.word(),))

        # Додавання викладачів
        for _ in range(NUMBER_TEACHERS):
            cur.execute("INSERT INTO teachers (fullname) VALUES (?)", (fake.name(),))
        
         # Додавання предметів 
        for _ in range(NUMBER_SUBJECTS):
            cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake.word(), (random.randint(1, NUMBER_TEACHERS))))

        # Додавання студентів і оцінок 
        for _ in range(NUMBER_STUDENTS):
            cur.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?) RETURNING id",
                        (fake.name(), random.randint(1, NUMBER_GROUPS)))
            for _ in range(NUMBER_GRADES):
                cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                        (random.randint(1, NUMBER_STUDENTS), random.randint(1, NUMBER_SUBJECTS), random.randint(0, 100), fake.date_this_year()))
      
        # Фіксуємо наші зміни в БД
        con.commit()

