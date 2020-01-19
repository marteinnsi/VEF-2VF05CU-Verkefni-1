from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route("/")
def route_index():
    return """
    <p>Hello world</p>
    <a href="/http">Http</a>
    <a href="/wolf">Úlfurinn</a>
    """

@app.route("/http")
def route_http():
    return app.send_static_file("html/http.html")

@app.route("/wolf")
def route_wolf():
    return app.send_static_file("html/wolf.html")

@app.route("/static/<dir>/<file>")
def route_static(dir, file):
    if dir in ["css", "img", "js"]:
        return app.send_static_file(f"{dir}/{file}")
    abort(404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)