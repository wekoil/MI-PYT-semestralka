import requests
import hmac
import json
import configparser
import click
import datetime

"""This file is used to add event to your scheduler"""

def validate_date(ctx, param, value):
    try:
        datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return value
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")

@click.command()
@click.option('-u', '--url', 'url', required=False, default='http://127.0.0.1:5000', help='Where is your service running.')

@click.option('-n', '--name', 'name', required=True, help='Name of the event.')

@click.option('-w', '--when', 'when', required=True, help='When to trigger the event.', callback=validate_date)

@click.option('-h', '--how', 'how', default='mail', show_default=True,
                type=click.Choice(['mail', 'slack', 'whatsapp'], case_sensitive=False), required=False, help='Via which channel send the message.')

@click.option('-m', '--message', 'message', required=False, default=None, help='Message body.')

@click.option('-s', '--subject', 'subject', required=False, default=None, help='Subject (for mail only).')

@click.option('-r', '--receiver', 'receiver', required=False, default=None, help='Receiver of the message.')

def run(url, name, when, how, message, subject, receiver):

    try:
        CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']
    except:
        CREDENTIALS_FILE = 'credentials.cfg'

    config = configparser.ConfigParser()
    with open(CREDENTIALS_FILE) as f:
        config.read_file(f)

    secret = config['web']['secret']
#  JSON = str('{"name": "' +  + '", "when": "2220-01-30 19:25:00", "how": "mail", "message": "novej event", "subject": "predmet"}')
    JSON = str('{"name": "' + name + '", "when": "' + when + '", "how": "' + how)
    
    if message != None:
        JSON += '", "message": "' + message
    if subject != None:    
        JSON += '", "subject": "' + subject
    if receiver != None:
        JSON += '", "receiver": "' + receiver
    
    JSON += '"}'

    mac = hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest()

    p = requests.request(method = 'post', url=str(url + '/add'), json=json.loads(JSON), headers={"Signature": "sha1={}".format(mac)})

    print(p)

if __name__ == '__main__':
    run()