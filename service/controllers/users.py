import json

import cerver.utils

from errors import *

from models.user import *

def todo_users_register (body_json):
	error = TODO_ERROR_NONE

	if body_json is not None:
		user_values = json.loads (body_json.contents.str)

		email = user_values['email']
		name = user_values['name']
		username = user_values['username']
		password = user_values['password']
		confirm = user_values['confirm']
		
		if email and name and username and password and confirm:
			found = user_find_by_email (email)
			if found is None:
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
