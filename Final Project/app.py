# from flask import Flask

# app = Flask(__name__)

# @app.route("/hello")
# def hello():
# 	return "Hello World!"


# @app.route("/goodbye")
# def goodbye():
# 	return "Goodbye World!"

# @app.route("/")
# def name():
# 	return "My name is saja!"

# @app.route("/saso")
# def saso():
# 	return "My nikename is soso!"


# if __name__=="__main__":
# 	app.run(port = 4000, debug=True)
###############################3
# from flask import Flask
# import random

# app = Flask(__name__)

# @app.route("/quote")
# def quote():
# 	a=["Hello!","my name is saja","I am 16 years","I  love the black color"]
# 	x=random.randint(0,len(a)-1)
# 	# x=(random.choice(a))

# 	return a[x]

# if __name__=="__main__":
# 	app.run(port = 4000, debug=True)	
###############################3
# from flask import Flask,render_template
# app = Flask(__name__)


# @app.route("/")
# def website():
# 	return  render_template("personal.html")

# @app.route("/wow.html")
# def a():
# 	return render_template("wow.html")


# if __name__=="__main__":
# 	app.run(debug=True)
#####################################

# from flask import Flask, render_template,request
# app = Flask(__name__)


# @app.route("/personal")
# def website():
# 	return render_template("personal.html",name="Welcom to my Home Page")

# @app.route("/wow.html")
# def a():
# 	return render_template("wow.html")

# @app.route("/")
# def homaa():
# 	return render_template("home.html",name="Welcom to my Home Page")

# @app.route("/form")
# def forma():
# 	return render_template("forms.html",name="Welcom to my Home Page")

# @app.route("/char")
# def char():
# 	return render_template("characters.html",name="Welcom to my Home Page")

# @app.route("/submit", methods=["POST"])
# def submit():
# 	myfirstname=request.form["firstName"]
# 	mylastname=request.form["lastName"]
# 	mypassword=request.form["Password"]

# 	return render_template("submit.html", nameOne=myfirstname, nameTwo=mylastname, password=mypassword)
	
# if __name__=="__main__":
# 	app.run(port=3000,debug=True)
####################################

from flask import Flask, render_template,request
app = Flask(__name__)


@app.route("/")
def websi():
	return render_template("HOME.html")

@app.route("/his")
def W():
	return render_template("History.html")
@app.route("/our")
def e():
	return render_template("ourteam.html")
@app.route("/form")
def f():
	return render_template("forms.html")	
@app.route("/vid")

def s():
	return render_template("vid.html")
@app.route("/submit", methods=["POST"])
def sub():
	myfeedback=request.form["feedBack"]
	mychange=request.form["Change"]


	return render_template("submit.html", feedBack=myfeedback, Change=mychange)
if __name__=="__main__":
	app.run(port=8500,debug=True)