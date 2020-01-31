Web
===

This module contains flask webserver.

Module can add, remove or list events which are scheduled.

Adding event
------------

Post event in JSON format to server/add address. Be sure to add Signature to header signed  with your secret to be sure you are permitted to procces the request.

Removing event
--------------

Post event id in JSON format to server/remove address. Sign with your secret as above.

Listing events
--------------

For listing of all scheduled events simply go to address server/list in your browser.

Posting secret
--------------

To make sure you are the one who is adding or removing the events you need to match the secret which is specified on the webserver.
This feature is here to make sure that somebody will not modify your events.

Loading calendar file
---------------------

On startup you can specify file in ics format. It will be used to load events from file to the scheduler.