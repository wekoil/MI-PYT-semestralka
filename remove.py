import requests
import hmac
import json
import configparser
import click

@click.command()
@click.option('-u', '--url', 'url', required=False, default='http://127.0.0.1:5000', help='Where is your service running.')

@click.argument('event_id', nargs=1, required=True)

def run(url, event_id):

    CREDENTIALS_FILE = 'credentials.cfg'

    config = configparser.ConfigParser()
    with open(CREDENTIALS_FILE) as f:
        config.read_file(f)

    secret = config['web']['secret']

    JSON = str('{"id": "' + event_id + '"}')

    mac = hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest()

    p = requests.request(method = 'post', url=str(url + '/remove'), json=json.loads(JSON), headers={"Signature": "sha1={}".format(mac)})

    print(p)

if __name__ == '__main__':
    run()