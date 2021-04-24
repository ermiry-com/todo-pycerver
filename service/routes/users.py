import ctypes
import json

import cerver

import todo
import runtime

import models.user

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
	
	body_json = json.loads (body.contents.str)

	name = body_json["name"]
	username = body_json["username"]
	email = body_json["email"]
	password = body_json["password"]
	confirm = body_json["confirm"]

	if name is not None and username is not None and email is not None and password is not None and confirm is not None:
		if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
			print ("name: ", name)
			print ("username: ", username)
			print ("email: ", email)
			print ("password: ", password)
			print ("confirm: ", confirm)

		response = cerver.http_response_json_msg (
			cerver.HTTP_STATUS_OK, "Users Works!".encode ('utf-8')
		)

		if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
			cerver.http_response_print (response)

		cerver.http_response_send (response, http_receive)
		cerver.http_response_delete (response)
	
	else:
		response = cerver.http_response_json_msg (
			cerver.HTTP_STATUS_BAD_REQUEST, "Missing user values!".encode ('utf-8')
		)

		if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
			cerver.http_response_print (response)
		
		cerver.http_response_send (response, http_receive)
		cerver.http_response_delete (response)

# POST /api/users/login
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def users_login_handler (http_receive, request):
	pass
