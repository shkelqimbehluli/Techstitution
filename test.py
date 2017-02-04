from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("hello.html")

@app.route("/about")
@app.route("/about/<string:name>/<int:age>")
def about(name=None):
    if name:
        return "Hello  " + name + "ka " + "Vjete"
    else:
        return "Hello there! i don't know your name !.."

if __name__ == "__main__":
    app.run(debug = True)
    