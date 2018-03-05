#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
#import sys

def read_rows_from_db1(sys_ip, dbname, uname, passwd, tablename):
	conn = None
	conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
	cur = conn.cursor()

	sqlquery = "SELECT * FROM %s" % tablename
	cur.execute(sqlquery)

	rows = cur.fetchall()
	print(rows)
	print(len(rows))

	for temp in rows:
		print(temp)
	print("")

	conn.close()
	return

def read_rows_from_db2(sys_ip, dbname, uname, passwd, tablename):
	conn = None
	conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
	cur = conn.cursor()

	sqlquery = "SELECT * FROM %s" % tablename
	cur.execute(sqlquery)
	rows = cur.fetchall()
	print(rows)

	sqlquery = "SELECT * FROM %s WHERE name='Ramesh'" % tablename
	cur.execute(sqlquery)
	rows = cur.fetchall()
	print(rows)
	print(len(rows))
	for row in rows:
		print(row)
	conn.close()
	return

def insert_rows_to_db(sys_ip, dbname, uname, passwd, tablename):
	conn = None
	conn = psycopg2.connect(database=dbname, user=uname, host=sys_ip, password=passwd)
	cur = conn.cursor()

	sqlquery = "INSERT INTO %s (name, phone, address, gender, dob) VALUES ('Naif', 77777777, 'Bangalore', 'M', '2010-05-11')" % tablename

	cur.execute(sqlquery)
	conn.commit()
	conn.close()

def insert_multiple_rows_to_db(dbname):
	conn = None
	conn = psycopg2.connect(database=dbname, user="bhagavan", host="127.0.0.1", password="jnjnuh")
	cur = conn.cursor()

	namedict = (
        {"type":"base ball", "color":"white",   "location":"south", "install_date":"2020-01-20"},
        {"type":"cricket",  "color":"white",   "location":"north", "install_date":"2020-01-20"},
        {"type":"tennis",   "color":"red",     "location":"west",  "install_date":"2020-08-10"}
        )

	cur.executemany("INSERT INTO playground(type, color, location, install_date) VALUES (%(type)s, %(color)s, %(location)s, %(install_date)s)", namedict)
	conn.commit()
	conn.close()
	return

def delete_rows_from_db(db):
	conn = None
	conn = psycopg2.connect(database="auradb", user="bhagavan", host="127.0.0.1", password="jnjnuh")
	cur = conn.cursor()

	sqlquery = "DELETE FROM %s WHERE type='tennis'" % "playground"
	cur.execute(sqlquery)
	conn.commit()
	conn.close()
	return

def main():
	db = "auradb"
	#read_rows_from_db1("127.0.0.1", "toys", "sumayya", "jnjnuh", "bblocks")
	#read_rows_from_db2("127.0.0.1", "auradb", "bhagavan", "jnjnuh", "contacts")

	#insert_rows_to_db("127.0.0.1", "auradb", "bhagavan", "jnjnuh", "contacts")
	#read_rows_from_db2("127.0.0.1", "auradb", "bhagavan", "jnjnuh", "contacts")
	insert_multiple_rows_to_db(db)
	#delete_rows_from_db(db)
	return


if (__name__ == "__main__"):
	main()

