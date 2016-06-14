from bottle import route, run, Bottle

app = Bottle()
@app.route("/test", method="GET")
def test():
	return "Hello WORLD!"

run(app, host="0.0.0.0", port=8081)