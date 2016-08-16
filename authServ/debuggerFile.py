class AuthService():

	_users = {}
	
	def login (self,user_name, password):
		"""
		if _users.has_key(user_name):
			if _users[nom_usuario] == password:
				#login correcto, enviar a home
			return true

		#return _users[(user_name,password)]
		"""
		return _users[(user_name, password)] if True else False


	def register (self,user_name, password):
		"""
		if _users.has_key(user_name):
			print user_name + " ya existe"
			return false
		else:
			if password != "":
				_users[user_name] = password
				#registro correcto, agregar a diccionario y mandar a login
				return true
			else:
				print "debe ingresar password"
				return false

		"""
		return _users[(user_name,password)] if true else false

	def helloWorld(self):
		return "helloWorld"

serv = AuthService()

print serv.login("seba",123)