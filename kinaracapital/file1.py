# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:39:26 2023

@author: Admin
"""

import sqlite3

conn = sqlite3.connect('kinarastudents.db')

conn.close()

def load_student_details():
    conn = sqlite3.connect('kinarastudents.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM student_info')
    student_details = cursor.fetchall()

    conn.close()

    return student_details

def get_students(page=1, page_size=10):
    conn = sqlite3.connect('kinarastudents.db')
    cursor = conn.cursor()

    offset = (page - 1) * page_size
    cursor.execute(f'SELECT * FROM student_info LIMIT {page_size} OFFSET {offset}')
    paginated_students = cursor.fetchall()

    conn.close()

    return paginated_students

def filter_students(filter_criteria, page=1, page_size=10):
    conn = sqlite3.connect('kinarastudents.db')
    cursor = conn.cursor()

    offset = (page - 1) * page_size
    cursor.execute(f"SELECT * FROM student_info WHERE name LIKE '%{filter_criteria}%' LIMIT {page_size} OFFSET {offset}")
    filtered_students = cursor.fetchall()

    conn.close()

    return filtered_students

# Testing the Load Student Details API
kinarastudents = get_students(page=1, page_size=10)
for student in kinarastudents:
    print(student)

# Testing the Server-side Filtering API
filtered_students = filter_students('Kiran', page=1, page_size=10)
for student in filtered_students:
    print(student)

