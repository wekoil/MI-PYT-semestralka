Usage
=====

Starting webserver
------------------

Simply run python file `python web.py`.

Adding jobs
-----------

For adding jobs when webserver is running use `add.py` python script.

.. code-block:: bash

    python add.py -n "Reminder" -w "2021-01-25 15:00:00" -h "mail" -m "You have exam tommorow!" -s "Exam tommorow"

Will add job into scheduler and send you mail at 2021-01-25 15:00:00.

Removing jobs
-------------

For removing jobs when webserver is running use `add.py` python script.

.. code-block:: bash

    python remove.py 1

Will remove event with id 1.

Load file
---------

For loading ics file with jobs to add use `load.py` python script.

.. code-block:: bash

    python load.py "events.ics"

Will load file events.ics into scheduler.

Configuration file
------------------

`config.cfg` is used for configuration of the messages.