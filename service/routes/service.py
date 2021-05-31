import ctypes

from cerver.http import HTTP_STATUS_OK
from cerver.http import http_response_print
from cerver.http import http_request_get_decoded_data
from cerver.http import http_response_json_key_value, http_response_json_msg
from cerver.http import http_response_send, http_response_delete

import todo
import runtime
import version

from controllers.users import todo_user_load_from_decoded_data

# GET /api/todo
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def main_handler (http_receive, request):
	response = http_response_json_msg (
		HTTP_STATUS_OK, "Todo Works!".encode ('utf-8')
	)

	if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
		http_response_print (response)
	
	http_response_send (response, http_receive)
	http_response_delete (response)

# GET /api/todo/version
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def version_handler (http_receive, request):
	v = '%s - %s' % (version.TODO_VERSION_NAME, version.TODO_VERSION_DATE)

	response = http_response_json_key_value (
		HTTP_STATUS_OK, "version".encode ('utf-8'), v.encode ('utf-8')
	)

	if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
		http_response_print (response)
	
	http_response_send (response, http_receive)
	http_response_delete (response)

# GET /api/todo/auth
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def auth_handler (http_receive, request):
	user = todo_user_load_from_decoded_data (
		http_request_get_decoded_data (request)
	)

	if (user):
		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			print (user)

		response = http_response_json_msg (
			HTTP_STATUS_OK, "okay!".encode ('utf-8')
		)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)
		
		http_response_send (response, http_receive)
		http_response_delete (response)

	else:
		response = http_response_json_error (
			HTTP_STATUS_BAD_REQUEST,
			"Bad user!".encode ('utf-8')
		)

		if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
			http_response_print (response)

		http_response_send (response, http_receive)
		http_response_delete (response)

# GET *
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_catch_all_handler (http_receive, request):
	response = http_response_json_msg (
		HTTP_STATUS_OK, "Todo Service!".encode ('utf-8')
	)

	if (todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT):
		http_response_print (response)
	
	http_response_send (response, http_receive)
	http_response_delete (response)
