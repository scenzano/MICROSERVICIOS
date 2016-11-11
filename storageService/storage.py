from bottle import Bottle, route, run, request, template, BaseRequest
import os
BaseRequest.MEMFILE_MAX = 1048576 # 1 mb to be able to receive picture on request

app = Bottle()

@app.route("/store", method="POST")
def create_response():
	answer = False
	data = request.json
	pictureBase64 = data["picture"]
	picFilter = data["filter"]
	path = "pictures/"
	if not os.path.exists(path):
		os.makedirs(path)
	try:
		f = open(path + "pepito.jpg", "wb")
		answer = True
		f.write(pictureBase64.decode('base64'))
	except IOError:
		print "Error: can\'t find file or read data"
	else:
		f.close()
	return {"status": "OK"} if answer else {"status": "can't open file"}

if __name__== "__main__":
	run(app, host="0.0.0.0", port=8082)
