import ctypes

from cerver.http import HTTP_STATUS_OK
from cerver.http import http_response_print
from cerver.http import http_response_json_key_value, http_response_json_msg
from cerver.http import http_response_send, http_response_delete

import todo
import runtime
import version

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

# GET /api/version
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
