from flask import Flask

from scheduler import Scheduler

app = Flask(__name__)

def run_scheduler():
    sch = Scheduler()
    sch.load_calendar('my.ics')

    sch.run()
    return sch

sch = run_scheduler()

# @app.route('/add', methods=['POST'])

@app.route('/list')
def list():
	return sch.get_events()


@app.route('/')
def index():
    return 'Running!'

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)