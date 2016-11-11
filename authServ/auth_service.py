from db_cnx import DbService

db = DbService()

class AuthService():

	def login(self,user_name,password):
		return True if db.get_user(user_name,password) else False

	
	def register(self,user_name, password):
		if db.get_user(user_name,password):
			print user_name + "ya existe"
			return False
		else:
			if password != "":
				if(db.insert_user(user_name,password)):
					return True
			else:
				print "Debe ingresar una password"
				return False



