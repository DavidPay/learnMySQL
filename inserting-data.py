#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-19-2018

from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user="localuser",password="local",database="employees",use_pure=True)
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")

add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

data_salary = {
  'emp_no': emp_no,
  'salary': 50000,
  'from_date': tomorrow,
  'to_date': date(9999, 1, 1),
}

cursor.execute(add_salary, data_salary)

cnx.commit()

cursor.close()

cnx.close()