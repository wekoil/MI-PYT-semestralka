Message
=======

This module is responsible for sending messages to you (as a reminder of something) or to someone else (if you dont want to remember all birthdays of your friends and sending them the same message every year).

The messages have configuration file where you need to specify some thing to work properly.

Mail
----

For sending mails you need to use some SMTP server which will handle the mail. I used google SMTP but there are much more you can use to match your needs.
You can specify to whom you want to send it as well as subject any body message.

Slack
-----

For sending slack messages you need to have token from slack and need to know identifier of the channel where you want to send the message.

Twilio - WhatsApp
-----------------

You can send WhatsApp messages via twilio. There are some problems however.
With twilio free account you can send messages only from your twilio number which did not match your number on whatsapp.
So if you send someone message he will not probably know that it is from you.
Second problem is you can only send messages to verified numbers.
To verify number to need to send some code from that number on twilio number.
I do not know how it is with premium account on twilio because i did not test it.

FB Messenger
------------

Is not implemented. I only found this resource https://github.com/carpedm20/fbchat which says that it violates facebook rules.
So I do not want to test it with my personal account and now it is 4 days of processing my fake one.