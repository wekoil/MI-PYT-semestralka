from flask import Flask, render_template

import flask

from scheduler import Scheduler

app = Flask(__name__)

def run_scheduler():
    sch = Scheduler()
    sch.load_calendar('my.ics')

    sch.run()
    return sch

sch = run_scheduler()

# @app.route('/add', methods=['POST'])

blueprint = flask.Blueprint('my', __name__)

@blueprint.route('/list')
def list():
	events = sch.get_events()
	return render_template('index.html', events=events)


@app.route('/')
def index():
    return 'Running!'

if __name__ == '__main__':
	app.register_blueprint(blueprint)
	app.run(debug=True,use_reloader=False)