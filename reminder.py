from abc import ABCMeta, abstractmethod

class Reminder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self): raise NotImplementedError

import smtplib, ssl
import configparser

class Mail(Reminder):
	def send(message=None):
	    config = configparser.ConfigParser()

	    with open('mail.cfg') as f:
	        config.read_file(f)

	    port = config['email']['port']
	    smtp_server = config['email']['smtp']
	    sender_email = config['email']['sender']
	    receiver_email = config['email']['receiver']

	    with open('gmail_password.txt') as f:  
	        password = f.read()
	    message = """Subject: Hi there

	    This message is sent from Python."""

	    context = ssl.create_default_context()
	    with smtplib.SMTP(smtp_server, port) as server:
	        server.ehlo()  # Can be omitted
	        server.starttls(context=context)
	        server.ehlo()  # Can be omitted
	        server.login(sender_email, password)
	        server.sendmail(sender_email, receiver_email, message)

	    print('Mail sent.')

import slack

class Slack(Reminder):
	def send(message=None, channel=None):

		with open('slack_token.txt') as f:  
		    slack_token = f.read()
		client = slack.WebClient(token=slack_token)

		text = "Hello from your app! :tada:"
		if message != None:
			text = message

		if channel == None:
			channel="CT04WDZC4"


		client.chat_postMessage(
		  channel=channel,
		  text=text
		)


if __name__ == '__main__':
    Slack.send()