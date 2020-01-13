from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route("/")
def route_index():
    return "Hello world"

@app.route("/http")
def route_http():
    return app.send_static_file("html/http.html")

@app.route("/wolf")
def route_wolf():
    return app.send_static_file("html/wolf.html")

@app.route("/static/<dir>/<file>")
def route_static(dir, file):
    if dir in ["css", "img"]:
        return app.send_static_file(f"{dir}/{file}")
    abort(404)
