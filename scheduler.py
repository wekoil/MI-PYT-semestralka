from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

import mail

def test_run():
    scheduler = BackgroundScheduler()

    x = datetime(2020, 1, 23, 10, 0)

    scheduler.add_job(mail.send_mail, next_run_time=x)
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
