import os
from pymongo import MongoClient

import todo

db = None

def todo_mongo_init ():
	global db

	client = MongoClient (todo.MONGO_URI)
	try:
		db = client.todo
		print ("Mongodb connected!")

	except:
		print ("Error connecting to Mongodb (Authentication Failed)")