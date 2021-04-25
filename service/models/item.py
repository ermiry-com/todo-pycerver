from bson import json_util
from bson.objectid import ObjectId

items = None

def item_model_init (db):
	global items
	items = db["items"]

class Item ():
	def __init__ (self):
		self.id = None

		self.user_oid = None

		self.title = None
		self.description = None

		self.date = None

		self.done = None
		self.completed = None

def items_get_all_by_user (user_id):
	result = None
	all_items = items.find ({'user': ObjectId (user_id)})
	if (all_items is not None):
		result = json_util.dumps (all_items)
