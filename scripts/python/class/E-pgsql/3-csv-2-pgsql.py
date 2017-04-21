#!/usr/bin/python
import csv
import psycopg2
import sys

fd = open('users-data.csv', 'rt')
reader = csv.reader(fd)

conn = None
conn = psycopg2.connect( database="postgres", user="postgres", host="127.0.0.1", password="jnjnuh")
cur = conn.cursor()

i = 0
for row in reader:
    if (i == 0):
        i = 1
        continue

    print row[0],
    print row[6]

    if (len(row[0]) == 0):
        print "=============Got row with name is zero"
    	cur.execute("INSERT INTO playground(type, color) VALUES (%s,%s)", (row[0], row[6]))


conn.commit()
fd.close()

cur.execute("SELECT * FROM playground")
rows = cur.fetchall()
print rows
exit(1)
for row in rows:
    print row


