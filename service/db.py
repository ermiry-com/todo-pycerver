import os
from pymongo import MongoClient

import cerver.utils

import todo

from models.item import item_model_init
from models.user import user_model_init

todo_db = None

def todo_mongo_init ():
	global todo_db

	result = False

	client = MongoClient (todo.MONGO_URI)
	try:
		todo_db = client.todo

		todo_db.command ('ping')

		cerver.utils.cerver_log_success (
			"Mongo DB connected!".encode ("utf-8")
		)

		item_model_init (todo_db)
		user_model_init (todo_db)

		result = True

	except Exception as e:
		cerver.utils.cerver_log_error (
			"Error connecting to Mongo DB".encode ("utf-8")
		)

		print (e)

	return result
