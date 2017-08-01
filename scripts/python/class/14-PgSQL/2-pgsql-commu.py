#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import sys

conn = None
conn = psycopg2.connect(database="gcontacts", user="bhagavan", host="127.0.0.1", password="jnjnuh")
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

add_row_query = "INSERT INTO my_contacts(id, name, phone, address, gender, dob) VALUES(30, 'Vachan', 9876588, 'Bangalore', 'M', '2017-05-11')"
cur.execute(add_row_query)
conn.commit()


exit(1)
'''
id |  name   | phone |  address  | gender |    dob     
----+---------+-------+-----------+--------+------------
  2 | Bhaavan |   966 | Bangalore | M      | 2017-05-11

    query = "INSERT INTO playground(type, color) VALUES (%s,%s)"
    data = (row[0], row[6])
    cur.execute(query, data)
'''


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
