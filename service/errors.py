import cerver

TODO_ERROR_NONE = 0
TODO_ERROR_BAD_REQUEST = 1
TODO_ERROR_MISSING_VALUES = 2
TODO_ERROR_BAD_USER = 3
TODO_ERROR_EXISTING_USER = 4
TODO_ERROR_SERVER_ERROR = 5

bad_request_error = None
bad_user_error = None
missing_values = None
existing_user_error = None
server_error = None

def todo_errors_init ():
	global bad_request_error
	global bad_user_error
	global missing_values
	global existing_user_error
	global server_error

	bad_request_error = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"Bad request!".encode ("utf-8")
	)

	bad_user_error = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"Bad user!".encode ("utf-8")
	)

	missing_values = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"Missing values!".encode ("utf-8")
	)

	existing_user_error = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_BAD_REQUEST,
		"error".encode ("utf-8"),
		"User already exists!".encode ("utf-8")
	)

	server_error = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_INTERNAL_SERVER_ERROR,
		"error".encode ("utf-8"),
		"Server error!".encode ("utf-8")
	)

def todo_error_send_response (todo_error, http_receive):
	if (todo_error == TODO_ERROR_NONE):
		pass

	if (todo_error == TODO_ERROR_BAD_REQUEST):
		cerver.http_response_send (bad_request_error, http_receive)

	if (todo_error == TODO_ERROR_MISSING_VALUES):
		cerver.http_response_send (missing_values, http_receive)

	if (todo_error == TODO_ERROR_BAD_USER):
		cerver.http_response_send (bad_user_error, http_receive)

	if (todo_error == TODO_ERROR_EXISTING_USER):
		cerver.http_response_send (existing_user_error, http_receive)

	if (todo_error == TODO_ERROR_SERVER_ERROR):
		cerver.http_response_send (server_error, http_receive)

def todo_errors_end ():
	global bad_request_error
	global bad_user_error
	global missing_values
	global existing_user_error
	global server_error

	cerver.http_response_delete (bad_request_error)
	cerver.http_response_delete (bad_user_error)
	cerver.http_response_delete (missing_values)
	cerver.http_response_delete (existing_user_error)
	cerver.http_response_delete (server_error)
