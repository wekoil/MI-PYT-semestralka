from abc import ABCMeta, abstractmethod

import smtplib, ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import slack

from twilio.rest import Client

CONFIG_FILE = 'config.cfg'

class Message:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def send(self): raise NotImplementedError

class Mail(Message):
    def send(subject=None, message=None, receiver=None):
        config = configparser.ConfigParser()
        with open(CONFIG_FILE) as f:
            config.read_file(f)

        port = config['email']['port']
        smtp_server = config['email']['smtp']
        sender_email = config['email']['sender']
        receiver_email = config['email']['receiver']

        with open('gmail_password.txt') as f:  
            password = f.read()

        if message == None:
            message = 'Default mail body.'

        mail_message = MIMEMultipart("alternative")
        mail_message["Subject"] = subject
        mail_message["From"] = sender_email
        mail_message["To"] = receiver_email
        part = MIMEText(message, "plain")
        mail_message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, mail_message.as_string())

class Slack(Message):
    def send(message=None, channel=None):

        with open('slack_token.txt') as f:  
            slack_token = f.read()
        client = slack.WebClient(token=slack_token)

        if message == None:
            message = "Hello from your app! :tada:"

        if channel == None:
            config = configparser.ConfigParser()
            with open(CONFIG_FILE) as f:
                config.read_file(f)
            channel = config['slack']['channel']


        client.chat_postMessage(
          channel=channel,
          text=message
        )

class WhatsApp(Message):
    def send(receiver=None, message=None):
        config = configparser.ConfigParser()
        with open('twilio.cfg') as f:
            config.read_file(f)
        sid = config['twilio']['SID']
        token = config['twilio']['TOKEN']

        # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
        client = Client(sid, token)

        with open(CONFIG_FILE) as f:
            config.read_file(f)
        sender = config['twilio']['sender']

        # this is the Twilio sandbox testing number
        from_whatsapp_number='whatsapp:{}'.format(sender)

        if receiver == None:
            receiver = config['twilio']['receiver']

        # replace this number with your own WhatsApp Messaging number
        to_whatsapp_number='whatsapp:{}'.format(receiver)

        if message == None:
            message = 'Nazdar'

        client.messages.create(body=message,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)


if __name__ == '__main__':
    WhatsApp.send(message='Nazdar', receiver='+420775960345')