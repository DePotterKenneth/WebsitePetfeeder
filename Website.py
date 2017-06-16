from flask import Flask
from flask import render_template
from flask import request
from flask import abort
from dbsecurity.dbconn import DbConnection
import os
instance_db = DbConnection("petfeeder_db")

app = Flask(__name__)


@app.route('/')
def live():
    sql = ('SELECT millilitres_left, timestamp FROM petfeeder_db.tbldrinklog where date(timestamp) = current_date();')
    result = instance_db.query(sql, dictionary=True)
    drink_time_list = []
    drink_value_list = []

    for item in range(0, len(result)):
        record = result[item]
        drink_time_list.append(record['timestamp'])
        drink_value_list.append(record['millilitres_left'])

    print(drink_value_list)
    print(drink_time_list)

    return render_template('index.html', drink_time_list=drink_time_list, drink_value_list=drink_value_list)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/settings', methods=['GET','POST'])
def settings():
    instantie_db = DbConnection('petfeeder_db')

    if request.method == 'POST':
        try:
            # sql = ('update tblsettings set led_alarm_enabeld = %(led_alarm_enabeld)s where settings_id = 1;')
            #
            # params = {
            #     'led_alarm_enabeld': int(request.form['led_alarm_enabeld'])
            # }
            #
            # instantie_db.execute(sql, params)

            vae = request.form['led_alarm_enabeld']

            print(vae)

            return render_template('settings.html')
        except:
            abort(400)
    else:
        return render_template('settings.html')

@app.route('/about')
def about():
    return render_template('about.html')

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