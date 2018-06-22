#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-19-2018

import mysql.connector
from mysql.connector import errorcode
'''
caution :
use_pure = True
if you don't do this, c extension Error will raise, and you can't catch it.
'''

def way1():
    try:
        cnx = mysql.connector.connect(user='localuser', password='local',host='localhost', use_pure=True)
   #     cnx.database = "sakil"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(err.msg)
    except Exception as e:
        pass
    else: #esle is corresponde to except. err goes except, no err goes else. finally always goes.
        cnx.close() 

def way2():
    from mysql.connector import connection
    try:
        cnx = connection.MySQLConnection(user='localuser', password='local')
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        cnx.close()

way1()
'''
config = {
  'user': 'scott',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,

  "use_pure":False
}

cnx = mysql.connector.connect(**config)

cnx.close()
'''