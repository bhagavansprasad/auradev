#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import sys

conn = None
conn = psycopg2.connect( database="gcontacts", user="bhagavan", host="127.0.0.1", password="jnjnuh")
cur = conn.cursor()

cur.execute("SELECT * FROM my_contacts")
rows = cur.fetchall()
print rows
print len(rows)
for row in rows:
    print row

cur.execute("SELECT * FROM my_contacts WHERE name='Bhaavan'")
rows = cur.fetchall()
print rows
print len(rows)
for row in rows:
    print row


'''
namedict = (
        {"type":"ball",     "color":"white",   "location":"south", "install_date":"2020-01-20"},
        {"type":"cricket",  "color":"white",   "location":"north", "install_date":"2020-01-20"},
        {"type":"tennis",   "color":"red",     "location":"west",  "install_date":"2020-08-10"}
        )

cur.executemany("INSERT INTO playground(type, color, location, install_date) VALUES (%(type)s, %(color)s, %(location)s, %(install_date)s)", namedict)
'''


''' 
''' 
