from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

from message import Mail, Slack, WhatsApp

from ics import Calendar, Event

import json

class Scheduler():
    def __init__(self):
        self.is_running = False
        self.scheduler = BackgroundScheduler()
        self.supported = ['mail', 'slack', 'whatsapp']

    def process_event(self, event):
        event_description = json.loads(event.description)

        message = 'This is default message.'
        if 'message' in event_description:
            message = event_description['message']

        receiver = None
        if 'receiver' in event_description:
            receiver = event_description['receiver']

        if not event_description['how'] in self.supported:
            raise NameError('Unknown option. Only mail, slack and whatsapp are supported now.')

        if event_description['how'] == 'mail':
            self.scheduler.add_job(Mail.send, next_run_time=event.begin.datetime, kwargs = dict(message=message, receiver=receiver))

        if event_description['how'] == 'slack':
            self.scheduler.add_job(Slack.send, next_run_time=event.begin.datetime, kwargs = dict(message=message, channel=receiver))

        if event_description['how'] == 'whatsapp':
            self.scheduler.add_job(WhatsApp.send, next_run_time=event.begin.datetime, kwargs = dict(message=message, receiver=receiver))

    def get_events(self):
        events = []
        for event in self.scheduler.get_jobs():
            events.append(event.__str__())
        # print(events)
        return events


    def run(self):
        if not self.is_running:
            self.scheduler.start()
        self.is_running = True

    def stop(self):
        if self.is_running:
            self.scheduler.shutdown()
        self.is_running = False

    def read_calendar(self, file):
        with open(file) as f:  
            ics = f.read()
        return Calendar(ics)

    def load_calendar(self, calendar_file):
        c = self.read_calendar(calendar_file)

        for event in c.events:
            self.process_event(event)


def test_run():
    c = read_calendar('my.ics')

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

    

if __name__ == '__main__':
    test_run()
    # c = read_calendar()

    # for e in c.events:
    #     # d = dict(e.description)
    #     # print(d['how'])
    #     # print(e.description)
    #     d = json.loads(e.description)
    #     print(e.begin.datetime)
    #     print(type(e.begin.datetime))

    #     if 'how' in d:
    #         print(d['how'])
