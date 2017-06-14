from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # check omgevingsvariabele voor poort of neem 8080 als standaarc
    port = int(os.environ.get("PORT", 8080))
    host = "0.0.0.0" #luistert naar alle IP's i.p.v. enkel 127.0.0.1
    app.run(host=host, port=port, debug=True)
