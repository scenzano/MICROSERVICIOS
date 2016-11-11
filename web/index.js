var express 	= require("express");
var request 	= require("request");
var bodyParser 	= require("body-parser");
var cookieParser = require('cookie-parser');
var handlebars 	= require("express-handlebars")
	.create({defaultLayout: "main"});

var multer  	= require("multer");
var storage     = multer.memoryStorage();
var upload      = multer({ storage: storage });

var app         = express();
app.engine("handlebars", handlebars.engine);
app.set("view engine", "handlebars");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + "/public"));
app.use(cookieParser());


app.get("/", function(req, res){
	if(req.cookies.token){
        console.log("hay token");
        var userInfo = {
    		uri: "http://app:8081/auth",
    		method: "POST", 
    		headers: {
    			"Content-type": "application/json"
    		},
    		json: {
    			"token":req.cookies.token
		  }
    	}
    	request(userInfo, function(error, response, body){
    		console.log(body);
    		if(!error && response.statusCode == 200) {
    			if(body.status == "OK"){
    				res.redirect("/home");
    			} else{
    				res.redirect("/login");
    			}
    		}
    	});

	}else{
		res.redirect("login");
	}
});

//-------Home------------------

app.get("/home", function(req, res){
    //TODO check token
    if(req.cookies.token){
        var userInfo = {
            uri: "http://app:8081/auth",
            method: "POST", 
            headers: {
                "Content-type": "application/json"
            },
            json: {
                "token":req.cookies.token
          }
        }
        request(userInfo, function(error, response, body){
            console.log(body);
            if(!error && response.statusCode == 200) {
                if(body.status == "OK"){
                    res.render("home");
                } else{
                    res.redirect("/login");
                }
            }
        });

    }else{
        res.redirect("login");
    }
});

/*
app.get("/home/:id", function(req, res){

	var id = req.params.id;
    if(id==1){	
		res.render("home",{error_message: "Something went wrong..."});
	}
});
*/

//------Register-------------

app.get("/register", function(req, res){
	
	res.render("register");
});

app.post("/register", function(req, res){

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

app.get("/register/:id", function(req, res){

	var id = req.params.id;
    if(id==1){	
		res.render("register",{error_message: "User already exists"});
	}
});

//-----------Login-----------------------------

app.get("/login", function(req, res){
	
	res.render("login");
});

app.post("/login", function(req, res){

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
				res.cookie('token', body.token)
				res.redirect("/home");
			} else{
				res.redirect("/login/1");
			}
		}
	});
});


app.get("/login/:id", function(req, res){

	console.log(req.params.id);
	var id = req.params.id;
	if(id==1){
		res.render("login",{error_message: "AUTHENTICATION ERROR"});
	}
});


//-----------------New pic---------------------------------

app.get("/newpic", function(req, res){
    if(req.cookies.token){
        var userInfo = {
            uri: "http://app:8081/auth",
            method: "POST", 
            headers: {
                "Content-type": "application/json"
            },
            json: {
                "token":req.cookies.token
          }
        }
        request(userInfo, function(error, response, body){
            console.log(body);
            if(!error && response.statusCode == 200) {
                if(body.status == "OK"){
                    res.render("newpic");
                } else{
                    res.redirect("/login");
                }
            }
        });

    }else{
        res.redirect("login");
    }
});

app.post("/newpic", upload.single("picture"), function(req, res){

	if (req.file) {
		var filter 	= req.body.filter;
		var pictureB64 	= req.file.buffer.toString("base64");
		var picInfo = {
			uri: "http://storage:8082/store",
			method: "POST", 
			headers: {
				"Content-type": "application/json"
			},
			json: {
				"filter": filter,
				"picture": pictureB64,
			}
		}

		request(picInfo, function(error, response, body){
			console.log(body);
			if(!error && response.statusCode == 200) {
				if(body.status == "OK"){
					res.send("Thanks for the picture!");
				} else{
					res.redirect("/newpic/1");
				}
			}
		});
	}
});

app.get("/newpic/:id", function(req, res){

	console.log(req.params.id);
	var id = req.params.id;
	if(id==1){
		res.render("newpic",{error_message: "Picture not found"});
	}
});

//--------------------------------------------------

var server = app.listen(8080, "0.0.0.0", function() {
	var host = server.address().address;
	var port = server.address().port;
	console.log("app listening at http://%s:%s", host, port);
});


