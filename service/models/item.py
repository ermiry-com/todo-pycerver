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

def item_parse (item_values):
	item = Item ()

	item.id = str (item_values["_id"])

	item.user_id = str (item_values["user"])

	item.title = item_values["title"]
	item.description = item_values["description"]

	item.date = item_values["date"]

	item.done = item_values["done"]

	if ("completed" in item_values):
		item.completed = item_values["completed"]

	return item

def items_get_all_by_user (user_id):
	result = None
	all_items = items.find ({'user': ObjectId (user_id)})
	if (all_items is not None):
		result = json_util.dumps (all_items)

	return result

def item_get_by_id_and_user (item_id, user_id):
	return items.find_one ({
		'_id': ObjectId (item_id),
		'user': ObjectId (user_id)
	})

def item_get_by_id_and_user_to_json (item_id, user_id):
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

def item_update (item):
	retval = False

	result = items.update_one (
		{
			'_id': ObjectId (item.id),
			'user': ObjectId (item.user_id)
		},
		{
			'$set': {
				'title': item.title,
				'description': item.description,
			}
		}
	)

	if (result.modified_count == 1):
		retval = True

	return retval

def item_delete_by_id_and_user (item_id, user_id):
	retval = False

	result = items.delete_one ({
		'_id': ObjectId (item_id),
		'user': ObjectId (user_id)
	})

	if (result.deleted_count == 1):
		retval = True

	return retval
