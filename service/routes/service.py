import ctypes

import cerver

import todo
import runtime
import version

# GET /api/todo
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def main_handler (http_receive, request):
	response = cerver.http_response_json_msg (
		cerver.HTTP_STATUS_OK, "Todo Works!".encode ('utf-8')
	)

	if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)
	
	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)

# GET /api/version
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def version_handler (http_receive, request):
	v = '%s - %s' % (version.STATUS_VERSION_NAME, version.STATUS_VERSION_DATE)

	response = cerver.http_response_json_key_value (
		cerver.HTTP_STATUS_OK, "version".encode ('utf-8'), v.encode ('utf-8')
	)

	if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)
	
	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)

# GET *
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def todo_catch_all_handler (http_receive, request):
	response = cerver.http_response_json_msg (
		cerver.HTTP_STATUS_OK, "Todo Service!".encode ('utf-8')
	)

	if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
		cerver.http_response_print (response)
	
	cerver.http_response_send (response, http_receive)
	cerver.http_response_delete (response)
