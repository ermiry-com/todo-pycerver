import json

import models.user

def todo_users_register (body_json):
	retval = 1

	if body_json is not None:
		user_values = json.loads (body_json.contents.str)
		email = user_values['email']
		name = user_values['name']
		username = user_values['username']
		password = user_values['password']
		confirm = user_values['confirm']
		
		if email and name and username and password and confirm:
			pass

	return retval
