from flask import Flask, render_template,request
app = Flask(__name__)


@app.route("/")
def websi():
	return render_template("HOME.html")

@app.route("/personHala")
def websit():
	return render_template("mywebsite.html")
@app.route("/wow.html")
def j():
	return render_template("wow.html")

@app.route("/his")
def W():
	return render_template("History.html")
@app.route("/team")
def e():
	return render_template("abo.html")
@app.route("/form")
def f():
	return render_template("forms.html")	

@app.route("/personSaja")
def a():
	return render_template("personal.html")	

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