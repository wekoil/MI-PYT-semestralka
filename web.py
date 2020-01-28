from flask import Flask, render_template, request

import flask

from scheduler import Scheduler

app = Flask(__name__)

def run_scheduler():
    sch = Scheduler()
    sch.load_calendar('my.ics')

    sch.process_event(Scheduler.create_event(name='jmeno', when='2020-01-28 19:01:00', how='mail', message='novej event', subject='predmet'))

    sch.run()
    return sch

sch = run_scheduler()

# @app.route('/add', methods=['POST'])

blueprint = flask.Blueprint('my', __name__)

@blueprint.route('/list')
def list():
    events = sch.get_events()
    return render_template('index.html', events=events)

# {"name": "jmeno", "when": "2020-01-28 19:01:00", "how": "mail", "message": "novej event", "subject": "predmet"}

@app.route('/add', methods=['POST'])
def add_event():
    # print(request.headers)
    # print(request.get_json())
    for atr in ['name', 'when', 'how']:
    	if atr not in request.get_json():
    		abort(400)
    		
    return '', 200
    

@app.route('/')
def index():
    return 'Running!'

if __name__ == '__main__':
    app.register_blueprint(blueprint)
    app.run(debug=True,use_reloader=True)
