import json
import time

import cerver.utils

from errors import *
import runtime
import todo

from models.user import *

def todo_user_get_by_email (email):
	found = user_get_by_email (email)
	if (found is not None):
		return user_parse (found)

	return None

def todo_users_register (body_json):
	error = TODO_ERROR_NONE

	if (body_json is not None):
		user_values = json.loads (body_json.contents.str)

		email = user_values['email']
		name = user_values['name']
		username = user_values['username']
		password = user_values['password']
		confirm = user_values['confirm']
		
		if (email and name and username and password and confirm):
			found = user_get_by_email (email)
			if (found is None):
				# if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
				# 	print ("name: ", name)
				# 	print ("username: ", username)
				# 	print ("email: ", email)
				# 	print ("password: ", password)
				# 	print ("confirm: ", confirm)

				if (password == confirm):
					user = user_create (email, name, username, password)
					saved_user = user_insert (user)
					
					cerver.utils.cerver_log_success (
						"Created a new user!".encode ("utf-8")
					)

					print (user)

				else:
					cerver.utils.cerver_log_warning (
						"Passwords do not match!".encode ("utf-8")
					);

					error = TODO_ERROR_BAD_REQUEST

			else:
				cerver.utils.cerver_log_warning (
					"User already exists!".encode ("utf-8")
				);

				error = TODO_ERROR_EXISTING_USER

		else:
			error = TODO_ERROR_MISSING_VALUES

	else:
		error = TODO_ERROR_MISSING_VALUES

	return error

def todo_user_generate_token (http_receive, user):
	http_jwt = cerver.http_cerver_auth_jwt_new ();
	cerver.http_cerver_auth_jwt_add_value_int (http_jwt, "iat".encode ('utf-8'), int (time.time ()));
	cerver.http_cerver_auth_jwt_add_value (http_jwt, "id".encode ('utf-8'), user.id.encode ('utf-8'));
	cerver.http_cerver_auth_jwt_add_value (http_jwt, "name".encode ('utf-8'), user.name.encode ('utf-8'));
	cerver.http_cerver_auth_jwt_add_value (http_jwt, "username".encode ('utf-8'), user.username.encode ('utf-8'));
	cerver.http_cerver_auth_jwt_add_value (http_jwt, "role".encode ('utf-8'), "common".encode ('utf-8'));

	cerver.http_cerver_auth_generate_bearer_jwt_json (cerver.http_receive_get_cerver (http_receive), http_jwt)

	response = cerver.http_response_create (
		cerver.HTTP_STATUS_OK,
		cerver.http_jwt_get_json (http_jwt), cerver.http_jwt_get_json_len (http_jwt)
	)

	cerver.http_cerver_auth_jwt_delete (http_jwt)

	return response

def todo_users_login (body_json):
	error = TODO_ERROR_NONE
	user = None

	if (body_json is not None):
		user_values = json.loads (body_json.contents.str)

		email = user_values['email']
		password = user_values['password']

		if (email and password):
			user = todo_user_get_by_email (email)
			if todo.RUNTIME == runtime.RUNTIME_TYPE_DEVELOPMENT:
				print (user)
			
			if (user.password != password):
				error = TODO_ERROR_BAD_REQUEST

		else:
			error = TODO_ERROR_MISSING_VALUES

	else:
		error = TODO_ERROR_MISSING_VALUES

	return error, user
