#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2

conn1 = None
conn1 = psycopg2.connect( database="auradb", user="postgres", host="127.0.0.1", password="jnjnuh")
cur1 = conn1.cursor()
cur1.execute("CREATE TABLE pgs1 (rno INTEGER PRIMARY KEY, name VARCHAR, phno VARCHAR);")
conn1.commit()


