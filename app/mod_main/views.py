from flask import Blueprint,render_template

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
	return render_template("index.html")

@mod_main.route('/form')
def form():
	name = "TechStitution Py."
	return render_template("form.html",param1 = name )

@mod_main.route('/about')
def about():
	return render_template("about.html")