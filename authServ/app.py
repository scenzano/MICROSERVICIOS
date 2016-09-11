from bottle import Bottle, route, run, request, template
from auth_service import AuthService
from db_cnx import DbService

app = Bottle()
auth = AuthService()
db = DbService()

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
	db.init_mysql()
	run(app, host="0.0.0.0", port=8081)



