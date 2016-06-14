from db_cnx import DbService


db = DbService()


class AuthService():
	#usuarios = [("usuario","123")] #lista de tuplas
	_usuarios_dict = {"usuario":"123"} #diccionario
    

	def login(self,user_name,password):
		#if user_name in self._usuarios_dict and self._usuarios_dict[user_name] == password:
		if db.get_user(user_name,password):
			return True# login correcto
		else:
			return False

	
	def register(self,user_name, password):
		if user_name in self._usuarios_dict:
			print user_name + "ya existe"
			return False
		else:
			if password != "":
			#registro correcto , agregar a diccionario y mandar al login o home
				self._usuarios_dict[user_name] = password
				if(db.insert_user(user_name,password)):
					return True
			else:
			#password vacio
				print "Debe ingresar una password"
				return False

	def helloWorld(self):
		return "helloWorld"


