from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def start_server():
    host = '0.0.0.0'  # 0.0.0.0 means all available interfaces.
    port = 5000  # Change this to the desired port number.

    app.run(host=host, port=port)
    # app.run()
