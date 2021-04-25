import ctypes
import json

import cerver

from errors import *
import runtime
import todo

import controllers.users

# GET /api/users
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_handler (http_receive, request):
	response = cerver.http_response_json_msg (
		cerver.HTTP_STATUS_OK, "Users Works!".encode ('utf-8')
	)

	if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)

	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)

# POST /api/users/register
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_register_handler (http_receive, request):
	body = cerver.http_request_get_body (request)

	result = controllers.users.todo_users_register (body)

	if result == TODO_ERROR_NONE:
		response = cerver.http_response_json_msg (
			cerver.HTTP_STATUS_OK, "Created a new user!".encode ('utf-8')
		)

		if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
			cerver.http_response_print (response)

		cerver.http_response_send (response, http_receive)
		cerver.http_response_delete (response)

	else:
		todo_error_send_response (result, http_receive)

# POST /api/users/login
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_login_handler (http_receive, request):
	pass
