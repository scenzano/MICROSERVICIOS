from bottle import Bottle, route, run, request, template, BaseRequest
import os
BaseRequest.MEMFILE_MAX = 1048576 # 1 mb to be able to receive picture on request

app = Bottle()

@app.route("/create", method="POST")
def create_response():
	data = request.json
	pictureBase64 = data["picture"]
	picFilter = data["filter"]
	path = "pictures/"
	if not os.path.exists(path):
		os.makedirs(path)
	#filename = os.path.join(path, filename)
	fh = open(path + "pepito.jpg", "wb")
	fh.write(pictureBase64.decode('base64'))
	fh.close()
	return {"status": "OK"}

if __name__== "__main__":
	run(app, host="0.0.0.0", port=8082)



