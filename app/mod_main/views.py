from flask import Blueprint,render_template
from app import mongo

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
	db = mongo.db.arkep
	db.insert({"name" : "arkep"})
	return render_template("index.html")

@mod_main.route('/form')
def form():
	name = "TechStitution Py."
	return render_template("form.html",param1 = name )

@mod_main.route('/about')
def about():
	return render_template("about.html")