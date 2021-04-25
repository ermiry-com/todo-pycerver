import datetime

from bson import json_util
from bson.objectid import ObjectId

items = None

def item_model_init (db):
	global items
	items = db["items"]

class Item ():
	def __init__ (self):
		self.id = None

		self.user_id = None

		self.title = None
		self.description = None

		self.date = None

		self.done = False
		self.completed = None

def item_create (title, description, user_id):
	item = Item ()
	item.title = title
	item.description = description
	item.user_id = user_id
	item.date = datetime.datetime.utcnow ()

	return item

def items_get_all_by_user (user_id):
	result = None
	all_items = items.find ({'user': ObjectId (user_id)})
	if (all_items is not None):
		result = json_util.dumps (all_items)

	return result

def item_get_by_id_and_user (item_id, user_id):
	result = None
	found = items.find_one ({
		'_id': ObjectId (item_id),
		'user': ObjectId (user_id)
	})

	if (found is not None):
		result = json_util.dumps (found)

	return result

def item_insert (item):
	item.id = items.insert ({
		'title': item.title,
		'description': item.description,
		'user': ObjectId (item.user_id),
		'date': item.date,
		'done': item.done,
	})

	return item

def item_delete_by_id_and_user (item_id, user_id):
	retval = False

	result =  items.delete_one ({
		'_id': ObjectId (item_id),
		'user': ObjectId (user_id)
	})

	if (result.deleted_count == 1):
		retval = True

	return retval
