import requests
import hmac
import json

secret = '1234'
JSON = '{"name": "JMENO", "when": "2020-01-30 15:25:00", "how": "mail", "message": "novej event", "subject": "predmet"}'

mac = hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest()

p = requests.request(method = 'post', url='http://127.0.0.1:5000/add', json=json.loads(JSON), headers={"Signature": "sha1={}".format(mac)})

# print(JSON)

# print()

print(p)

# r = requests.post(p)

# print(r)