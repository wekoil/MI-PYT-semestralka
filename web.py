from flask import Flask

from scheduler import Scheduler

app = Flask(__name__)

def run_scheduler():
    sch = Scheduler()
    sch.load_calendar('my.ics')
    sch.run()

run_scheduler()

@app.route('/')
def index():
    return 'MI-PYT je nejlepší předmět na FITu!'
