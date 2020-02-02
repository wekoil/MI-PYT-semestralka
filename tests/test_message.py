from message import Mail, Slack, WhatsApp
import os

def test_mail():
    Mail.send()

def test_wrong_mail():
    os.environ['CONFIG_FILE'] = 'config_wrong.cfg'
    Mail.send()