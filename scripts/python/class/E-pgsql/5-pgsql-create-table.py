#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

conn1 = None
conn1 = psycopg2.connect( database="postgres", user="postgres", host="127.0.0.1", password="jnjnuh")
cur1 = conn1.cursor()
cur1.execute("CREATE TABLE pgs1 (rno INTEGER PRIMARY KEY, name VARCHAR, phno VARCHAR);")
conn1.commit()

conn2 = None
conn2 = psycopg2.connect( database="gcontacts", user="postgres", host="127.0.0.1", password="jnjnuh")
cur2 = conn2.cursor()
cur2.execute("CREATE TABLE gcs1 (rno INTEGER PRIMARY KEY, name VARCHAR, phno VARCHAR);")
conn2.commit()

