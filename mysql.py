#!/usr/bin/python
#使用 MySQLdb 模块连接 MySQL

#Filename: mysql.py
# coding=utf-8

import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="test", charset="utf8")
cursor = conn.cursor()
cursor.execute("select * from user")
records = cursor.fetchall()
for row in records:
	for r in row:
		print(r)
