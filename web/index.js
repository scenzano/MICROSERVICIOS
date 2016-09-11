var express = require("express");				
var request = require("request");
var bodyParser = require("body-parser"); 		
var handlebars = require("express-handlebars")
	.create({defaultLayout: "main"});			

var app = express();
app.use(bodyParser.urlencoded({extended : true}));
app.engine("handlebars", handlebars.engine);
app.set("view engine", "handlebars");

app.use(express.static(__dirname + '/public'));


app.get('/', function(req, res){
	//if user is NOT authenticated
	res.redirect("login");
});

//-------Home------------------

app.get('/home', function(req, res){
	//res.sendFile(__dirname + "/" + "home.html");
	res.render("home");
});

//------Register-------------

app.get('/register', function(req, res){
	//res.sendFile(__dirname + "/" + "register.html");
	res.render("register");
});

app.post('/register', function(req, res){

	var username = req.body.username;
	var password = req.body.password;
	var userInfo = {
		uri: "http://app:8081/register",
		method: "POST", 
		headers: {
			"Content-type": "application/json"
		},
		json: {
			"username": username,
			"password": password,
		}
	}

	request(userInfo, function(error, response, body){
		console.log(body);
		if(!error && response.statusCode == 200) {
			if(body.status == "OK"){
				res.redirect("/home");
			} else{
				res.redirect("/register/1");
			}
		}
	});
});

app.get('/register/:id', function(req, res){
	var id = req.params.id;
	if(id==1){
		//res.sendFile(__dirname + "/" + "register-1.html");
		res.render("register",{error_message: "User already exists"});
	}
});

//-----------Login-----------------------------

app.get('/login', function(req, res){
	//res.sendFile(__dirname + "/" + "login.html");
	res.render("login");
});

app.post('/login', function(req, res){

	var username = req.body.username;
	var password = req.body.password;
	var userInfo = {
		uri: "http://app:8081/login",
		method: "POST", 
		headers: {
			"Content-type": "application/json"
		},
		json: {
			"username": username,
			"password": password,
		}
	}

	request(userInfo, function(error, response, body){
		console.log(body);
		if(!error && response.statusCode == 200) {
			if(body.status == "OK"){
				res.redirect("/home");
			} else{
				res.redirect("/login/1");
			}
		}
	});
});


app.get('/login/:id', function(req, res){
	console.log(req.params.id);
	var id = req.params.id;
	if(id==1){
		//res.sendFile(__dirname + "/" + "login-1.html");
		res.render("login",{error_message: "AUTHENTICATION ERROR"});
	}
});


var server = app.listen(8080, "0.0.0.0", function() {
	var host = server.address().address;
	var port = server.address().port;
	console.log("app listening at http://%s:%s", host, port);
});


