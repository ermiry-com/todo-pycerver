users = None

def user_model_init (db):
	global users
	users = db["users"]

class User ():
	def __init__ (self):
		self.id = None

		self.email = None
		self.name = None
		self.username = None
		self.password = None

		self.iat = 0

		self.items_count = 0

	def __str__ (self):
		return f'User: \n\t{self.id} \n\t{self.email} \n\t{self.name} \n\t{self.username}'

def user_create (email, name, username, password=None):
	user = User ()
	user.email = email
	user.name = name
	user.username = username
	user.password = password

	return user

def user_find_by_email (email):
	return users.find_one ({'email': email})

def user_insert (user):
	user.id = users.insert ({
		'email': user.email,
		'name': user.name,
		'username': user.username,
		'password': user.password
	})

	return user
