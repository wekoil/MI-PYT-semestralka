from abc import ABCMeta, abstractmethod

import smtplib, ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import slack

CONFIG_FILE = 'config.cfg'

class Reminder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self): raise NotImplementedError

class Mail(Reminder):
	def send(subject=None, message=None):
	    config = configparser.ConfigParser()

	    with open(CONFIG_FILE) as f:
	        config.read_file(f)

	    port = config['email']['port']
	    smtp_server = config['email']['smtp']
	    sender_email = config['email']['sender']
	    receiver_email = config['email']['receiver']

	    with open('gmail_password.txt') as f:  
	        password = f.read()

	    text = """This message is sent from Python."""

	    if message != None:
		    text = message

	    mail_message = MIMEMultipart("alternative")
	    mail_message["Subject"] = subject
	    mail_message["From"] = sender_email
	    mail_message["To"] = receiver_email
	    part = MIMEText(text, "plain")
	    mail_message.attach(part)

	    context = ssl.create_default_context()
	    with smtplib.SMTP(smtp_server, port) as server:
	        server.ehlo()  # Can be omitted
	        server.starttls(context=context)
	        server.ehlo()  # Can be omitted
	        server.login(sender_email, password)
	        server.sendmail(sender_email, receiver_email, mail_message.as_string())

	    print('Mail sent.')

class Slack(Reminder):
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

class Facebook(Reminder):
	def send(whom=None, message=None):


if __name__ == '__main__':
    Slack.send(message='nevim')