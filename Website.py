from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route('/')
def live():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.errorhandler(401)
def throw_401(error):
    return render_template('error_pages/401.html', error=error)


@app.errorhandler(404)
def throw_404(error):
    return render_template('error_pages/404.html', error=error)

if __name__ == '__main__':
    # check omgevingsvariabele voor poort of neem 8080 als standaarc
    port = int(os.environ.get("PORT", 8080))
    host = "169.254.10.111" #luistert naar alle IP's i.p.v. enkel 127.0.0.1
    app.run(host=host, port=port, debug=True)
