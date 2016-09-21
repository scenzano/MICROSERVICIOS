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
	if (auth.login(username,password)):
		return {"status": "OK"}
	else:
		return {"status": "False"}


@app.route("/register", method="POST")
def register_response():
	data = request.json
	username = data["username"]
	password = data["password"]
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
	data = request.json
	param = data["param"]
	id = request.query.id
	ret = {"status": "OK", "param": param, "id": id}
	return ret


if __name__== "__main__":
	db.init_mysql()
	run(app, host="0.0.0.0", port=8081)