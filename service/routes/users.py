import ctypes
import json

from cerver.http import HTTP_STATUS_OK
from cerver.http import http_response_print
from cerver.http import http_request_get_body
from cerver.http import http_response_compile, http_response_json_msg
from cerver.http import http_response_send, http_response_delete

from errors import *
import runtime
import todo

import controllers.users

# GET /api/users
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_handler (http_receive, request):
	response = http_response_json_msg (
		HTTP_STATUS_OK, "Users Works!".encode ('utf-8')
	)

	if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
		http_response_print (response)

	http_response_send (response, http_receive)
	http_response_delete (response)

# POST /api/users/register
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_register_handler (http_receive, request):
	body = http_request_get_body (request)

	result = controllers.users.todo_users_register (body)

	if (result == TODO_ERROR_NONE):
		response = http_response_json_msg (
			HTTP_STATUS_OK, "Created a new user!".encode ('utf-8')
		)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

	else:
		todo_error_send_response (result, http_receive)

# POST /api/users/login
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_login_handler (http_receive, request):
	body = http_request_get_body (request)

	error, user = controllers.users.todo_users_login (body)

	if (error == TODO_ERROR_NONE):
		response = controllers.users.todo_user_generate_token (http_receive, user)
		http_response_compile (response)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

	else:
		todo_error_send_response (error, http_receive)
