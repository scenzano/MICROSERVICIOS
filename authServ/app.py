from bottle import Bottle, route, run, request, template
from auth_service import AuthService
from db_cnx import DbService
import jwt

app = Bottle()
auth = AuthService()
db = DbService()
secret = "34jdnsoe43029JnsKueJns-NSHensha238JneA"

@app.route("/login", method="POST")
def login_response():
	data = request.json
	username = data["username"]
	password = data["password"]
	token = jwt.encode({"username": username}, secret, algorithm='HS256')
	if (auth.login(username,password)):
		return {"status": "OK", "token" : token}
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

@app.route("/auth", method="POST")
def auth_response():
	data = request.json
	token = data["token"]
	try:
		decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
	except Exception as e:
		return {"status":"ERROR", "message":str(e)}
	return {"status": "OK", "username":decoded_token[u"username"]}


@app.route("/", method="GET")
@app.route("/hello/<name>", method="GET")	
def greet(name="Stranger"):
	return template ("Hello {{nombre}}", nombre=name)

if __name__== "__main__":
	db.init_mysql()
	run(app, host="0.0.0.0", port=8081)	