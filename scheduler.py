from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

from message import Mail, Slack, WhatsApp

from ics import Calendar, Event

import json

class Scheduler():
    """ This class handles event adding, removing and listing """
    def __init__(self):
        self.is_running = False
        self.scheduler = BackgroundScheduler()
        self.supported = ['mail', 'slack', 'whatsapp']
        self.counter = 0

    def process_event(self, event):
        """ Used adding jobs to scheduler. """
        event_description = json.loads(event.description)

        message = 'This is default message.'
        if 'message' in event_description:
            message = event_description['message']

        receiver = None
        if 'receiver' in event_description:
            receiver = event_description['receiver']

        subject = None
        if 'subject' in event_description:
            subject = event_description['subject']

        if not event_description['how'] in self.supported:
            raise NameError('Unknown option. Only mail, slack and whatsapp are supported now.')

        id = str(self.counter)

        if event_description['how'] == 'mail':
            self.scheduler.add_job(Mail.send, next_run_time=event.begin.datetime, kwargs = dict(message=message, receiver=receiver, subject=subject), id=id, name=event.name)

        if event_description['how'] == 'slack':
            self.scheduler.add_job(Slack.send, next_run_time=event.begin.datetime, kwargs = dict(message=message, channel=receiver), id=id, name=event.name)

        if event_description['how'] == 'whatsapp':
            self.scheduler.add_job(WhatsApp.send, next_run_time=event.begin.datetime, kwargs = dict(message=message, receiver=receiver), id=id, name=event.name)

        self.counter += 1

        return id

    def get_events(self):
        """
        Method returns list of scheduled events.
        """
        events = []
        for event in self.scheduler.get_jobs():
            function_name = str(event.func)
            events.append(str('ID: ' + event.id + ', Name: ' + event.__str__() + ' ' + function_name + ' ' + str(event.kwargs)))
        # print(events)
        return events


    def run(self):
        """
        Starts scheduler.
        """
        if not self.is_running:
            self.scheduler.start()
        self.is_running = True

    def stop(self):
        """
        Stops scheduler.
        """
        if self.is_running:
            self.scheduler.shutdown()
        self.is_running = False

    def read_calendar(self, file):
        """
        Method will read specified calendar from file in ics format.
        """
        with open(file) as f:  
            ics = f.read()
        return Calendar(ics)

    def load_calendar(self, calendar_file):
        """
        Method will add events from calendar to scheduler.
        """
        c = self.read_calendar(calendar_file)

        for event in c.events:
            self.process_event(event)

    @staticmethod
    def create_description(how='mail', receiver=None, message=None, subject=None):
        """
        Method will create description to match for adding job.
        """
        d = '{'
        d += '"how": "'
        d += how
        d += '"'

        if receiver != None:
            d += ', "receiver": "'
            d += receiver
            d += '"'

        if message != None:
            d += ', "message": "'
            d += message
            d += '"'

        if subject != None:
            d += ', "subject": "'
            d += subject
            d += '"'

        d += '}'
        # print(d)
        return d

    @staticmethod
    def create_event(name, when, how='mail', receiver=None, message=None, subject=None):
        """
        Method will create event from specified parameters which can be later added to scheduler.
        """
        e = Event()
        e.name = name
        e.begin = when
        e.description = Scheduler.create_description(how, receiver, message, subject)

        return e

    def remove_event(self, event_id):
        """
        Remove event from scheduler specified by his id.
        """
        try:
            self.scheduler.remove_job(str(event_id))
            return True
        
        except:
            return False
