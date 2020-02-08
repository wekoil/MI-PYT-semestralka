import requests
import hmac
import json
import configparser
import click

@click.command()
@click.argument('calendar_file', nargs=1, required=True)

def run(calendar_file):

    try:
        CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']
    except:
        CREDENTIALS_FILE = 'credentials.cfg'

    config = configparser.ConfigParser()
    with open(CREDENTIALS_FILE) as f:
        config.read_file(f)

    secret = config['web']['secret']

    JSON = str('{"file_name": "' + calendar_file + '"}')

    # print(JSON)

    mac = hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest()

    p = requests.request(method = 'post', url='http://127.0.0.1:5000/load', json=json.loads(JSON), headers={"Signature": "sha1={}".format(mac)})

    print(p)

if __name__ == '__main__':
    run()