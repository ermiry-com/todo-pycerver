import os
from pymongo import MongoClient

import cerver.utils

import todo

from models.user import user_model_init
from models.item import item_model_init

todo_db = None

def todo_mongo_init ():
	global todo_db

	client = MongoClient (todo.MONGO_URI)
	try:
		todo_db = client.todo
		cerver.utils.cerver_log_success (
			"Mongo DB connected!".encode ("utf-8")
		)

		user_model_init (todo_db)
		item_model_init (todo_db)

	except:
		cerver.utils.cerver_log_error (
			"Error connecting to Mongo DB".encode ("utf-8")
		)
