import requests
import hmac
import json
import configparser

CREDENTIALS_FILE = 'credentials.cfg'

config = configparser.ConfigParser()
with open(CREDENTIALS_FILE) as f:
    config.read_file(f)

secret = config['web']['secret']

JSON = '{"id": "4"}'

mac = hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest()

p = requests.request(method = 'post', url='http://127.0.0.1:5000/remove', json=json.loads(JSON), headers={"Signature": "sha1={}".format(mac)})

print(p)