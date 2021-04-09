class User ():
	def __init__ (self, id, iat, email, name, username):
		self.id = id

		self.email = email
		self.name = name
		self.username = username
		self.password = None

		self.iat = iat

		self.items_count = 0

	def __str__ (self):
		return f'User: \n\t{self.id} \n\t{self.email} \n\t{self.name} \n\t{self.username}'