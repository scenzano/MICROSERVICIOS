from bottle import Bottle, route, run, request, template
from auth_service import AuthService
from db_cnx import DbService

#Bottle es una clase que esta publicada a nivel paquete
#podria ser import bottle.route
#en python no se usa camelCase se usa guion bajo, en la clases si se usa camelCase

#instanciamos en app bottle

app = Bottle()
auth = AuthService()
db = DbService()

#----METODO PARA TESTEAR CONEXION CON AUTH---
"""
@app.route("/hello", method="GET")
def hello():
	if auth.login("usuario",123):
		return "hola" 
	else:
		return "no anduvo"
"""

#---------------------------------------------


@app.route("/login", method="POST")
def login_response():
	data = request.json
	username = data["username"]
	password = data["password"]
	#ret = {"status": "OK"}
	if (auth.login(username,password)):
		return {"status": "OK"}
	else:
		return {"status": "False"}



@app.route("/register", method="POST")
def register_response():
	data = request.json
	username = data["username"]
	password = data["password"]
	#ret = {"status": "OK"}
	if (auth.register(username,password)):
		return {"status": "OK"}
	else:
		return {"status": "False"}

#vamos a crear dos rutas nuevas "/" y la de abajo que hacen lo mismo
@app.route("/", method="GET")
@app.route("/hello/<name>", method="GET")	
def greet(name="Stranger"):
	return template ("Hello {{nombre}}", nombre=name)

@app.route("/param", method="POST")
def hello_json():
	data = request.json   #viendo info del body
	param = data["param"]
	id = request.query.id #Con el parametro query puedo ver los query que mando en la URL
						  #falta ver la info de los header
	ret = {"status": "OK", "param": param, "id": id}
	return ret
# una de las mejores cosas es que python tiene como nativo JSON. uno abre las llaves y ya se sabe que es un JSON

if __name__== "__main__":
	#db.test_mysql()
	#run(app, host="127.0.0.1", port=8081)
	run(app, host="0.0.0.0", port=8081) # 0.0.0.0 para poder conectarme con la app dentro de docker



