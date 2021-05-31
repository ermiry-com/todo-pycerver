import ctypes
import json

from cerver.http import HTTP_STATUS_OK, HTTP_STATUS_NOT_FOUND
from cerver.http import http_request_get_decoded_data
from cerver.http import http_request_get_body, http_request_get_param_at_idx
from cerver.http import http_response_render_json
from cerver.http import http_response_json_msg, http_response_json_error
from cerver.http import http_response_print, http_response_send, http_response_delete

from errors import *
import runtime
import todo

import controllers.items
import controllers.users

# GET /api/todo/items
# get all the authenticated user's items
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_items_handler (http_receive, request):
	user = controllers.users.todo_user_load_from_decoded_data (
		http_request_get_decoded_data (request)
	)
	
	result = controllers.items.todo_items_get_all_by_user (user)
	if (result is not None):
		http_response_render_json (
			http_receive, HTTP_STATUS_OK, result.encode ("utf-8"), len (result)
		)

	else:
		response = json.dumps ({
			"items": []
		})

		http_response_render_json (
			http_receive, HTTP_STATUS_OK, response.encode ("utf-8"), len (response)
		)

# POST /api/todo/items
# a user has requested to create a new item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_create_handler (http_receive, request):
	user = controllers.users.todo_user_load_from_decoded_data (
		http_request_get_decoded_data (request)
	)

	body = http_request_get_body (request)

	result = controllers.items.todo_item_create (user, body)

	if (result == TODO_ERROR_NONE):
		response = http_response_json_msg (
			HTTP_STATUS_OK,
			"Created a new item!".encode ('utf-8')
		)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

	else:
		todo_error_send_response (result, http_receive)

# GET /api/todo/items/:id/info
# returns information about an existing item that belongs to a user
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_get_handler (http_receive, request):
	user = controllers.users.todo_user_load_from_decoded_data (
		http_request_get_decoded_data (request)
	)

	item_id_str = http_request_get_param_at_idx (
		request, 0
	)

	result = controllers.items.todo_item_get_by_id_and_user_to_json (
		item_id_str, user
	)

	if (result is not None):
		http_response_render_json (
			http_receive, HTTP_STATUS_OK, result.encode ("utf-8"), len (result)
		)

	else:
		response = http_response_json_error (
			HTTP_STATUS_NOT_FOUND,
			"Item not found".encode ('utf-8')
		)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

# PUT /api/todo/items/:id/update
# a user wants to update an existing item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_update_handler (http_receive, request):
	user = controllers.users.todo_user_load_from_decoded_data (
		http_request_get_decoded_data (request)
	)

	item_id_str = http_request_get_param_at_idx (
		request, 0
	)

	body = http_request_get_body (request)

	result = controllers.items.todo_item_update (
		item_id_str, user, body
	)

	if (result == TODO_ERROR_NONE):
		response = http_response_json_msg (
			HTTP_STATUS_OK,
			"Updated item!".encode ('utf-8')
		)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

	else:
		todo_error_send_response (result, http_receive)

# DELETE /api/todo/items/:id/remove
# deletes an existing user's item
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_item_delete_handler (http_receive, request):
	user = controllers.users.todo_user_load_from_decoded_data (
		http_request_get_decoded_data (request)
	)

	item_id_str = http_request_get_param_at_idx (
		request, 0
	)

	result = controllers.items.todo_item_delete_by_id_and_user (
		item_id_str, user
	)

	if (result):
		response = http_response_json_msg (
			HTTP_STATUS_OK,
			"Deleted item!".encode ('utf-8')
		)

		if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

	else:
		response = http_response_json_error (
			HTTP_STATUS_NOT_FOUND,
			"Item not found".encode ('utf-8')
		)

		if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)
	
