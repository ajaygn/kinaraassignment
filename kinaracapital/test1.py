# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:12:14 2023

@author: Admin
"""

import sqlite3

conn = sqlite3.connect('kinarastudents.db')
print("enter the student id")
r = input()
print("enter student name")
nm = input()
print("enter student total_marks")
mrks = input()
print("enter student class")
cla = input()
print("enter student city")
city=input()



query ="insert into student_info(id,Name,Total_Marks,Class,City) values (" + r +",'" + nm + "'," + mrks +"," + cla + ",'" + city + "')"
conn.execute(query)
conn.commit()
conn.close()

print("Data Saved ....")

