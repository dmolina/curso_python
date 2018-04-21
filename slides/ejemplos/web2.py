from flask import Flask
app = Flask(__name__)


@app.route("/saluda/<name>")
@app.route("/saluda")
def hello(name="desconocido"):
    return "Hola {}".format(name)


if __name__ == '__main__':
    app.run()
