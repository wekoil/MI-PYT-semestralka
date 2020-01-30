import requests
import hmac
import json

secret = '1234'
JSON = '{"name": "jmeno", "when": "2020-01-28 19:01:00", "how": "mail", "message": "novej event", "subject": "predmet"}'

p = requests.request(method = 'post', url='http://127.0.0.1:5000/add', json=json.loads(JSON), headers={"Signature": "sha1=2cebbfbba66855b419f9015b0b387b380016d779"})

print(JSON)

print(hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest())

print(p)

# r = requests.post(p)

# print(r)