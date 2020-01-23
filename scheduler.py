from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

from reminder import Mail, Slack

from ics import Calendar, Event

import json

def process_event(event, scheduler):
    event_description = json.loads(event.description)

    message = 'This is default message.'

    if 'message' in event_description:
        message = event_description['message']

    if event_description['how'] == 'mail':
        scheduler.add_job(Mail.send, next_run_time=event.begin.datetime, kwargs = dict(message=message))

    else:
        if event_description['how'] == 'slack':
            scheduler.add_job(Slack.send, next_run_time=event.begin.datetime, kwargs = dict(message=message))

        else:
            raise NameError('Unknown option. Only mail and slack are supported now.')

    


def test_run():
    c = load_calendar()

    scheduler = BackgroundScheduler()

    # x = datetime(2020, 1, 23, 12, 10)

    for e in c.events:
        process_event(e, scheduler)

    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()

def load_calendar():
    with open('my.ics') as f:  
        ics = f.read()
    return Calendar(ics)

if __name__ == '__main__':
    test_run()
    # c = load_calendar()

    # for e in c.events:
    #     # d = dict(e.description)
    #     # print(d['how'])
    #     # print(e.description)
    #     d = json.loads(e.description)
    #     print(e.begin.datetime)
    #     print(type(e.begin.datetime))

    #     if 'how' in d:
    #         print(d['how'])
