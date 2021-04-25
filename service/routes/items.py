import ctypes
import json

import cerver

import controllers.items
import controllers.users

# GET /api/todo/items
# get all the authenticated user's items
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_items_handler (http_receive, request):
	user = controllers.users.todo_user_load_from_decoded_data (
		cerver.http_request_get_decoded_data (request)
	)
	
	result = controllers.items.todo_items_get_all_by_user (user)
	if (result is not None):
		cerver.http_response_render_json (
			http_receive, result, len (result)
		)

	else:
		items = {
			"items": []
		}

		response = json.dumps (items)
		cerver.http_response_render_json (
			http_receive, response.encode ("utf-8"), len (response)
		)

# POST /api/todo/items
# a user has requested to create a new item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_create_handler (http_receive, request):
	pass

# GET /api/todo/items/:id/info
# returns information about an existing item that belongs to a user
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_get_handler (http_receive, request):
	pass

# PUT /api/todo/items/:id/update
# a user wants to update an existing item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_update_handler (http_receive, request):
	pass

# DELETE /api/todo/items/:id/remove
# deletes an existing user's item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_delete_handler (http_receive, request):
	pass
