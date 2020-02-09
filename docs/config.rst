Config file
===========

In order to get whole module working you need to set up configuration file.

Twilio
------

For twilio you need to set up your twilio number and in case of default sending messages to you your phone number.

Email
-----

For email communication you need to set up smtp server, port number and sender email, which has to match your password in credentials file. In case of default sending emails to you, set up email address where you want to receive emails.

Slack
-----

If you want to use default slack messages without receiver you need to set up default one. In case of slack you need to know id of channel where you want to send messages.
If you want to get your id go to web version of slack and click onto specified channel or direct message. Then copy identifier after slash from web address.

Example https://app.slack.com/client/HCHKRDTN/AEIOU in this case copy "AEIOU" into yout config file.
