import pytest
from web import *
import flexmock
import requests

import hmac
import json
import configparser

def test_verify_right_signature(capsys):
	req = flexmock(requests.Request(), headers={'Signature': 'sha1=aa6be43a6f16941bc73885ac233bc5c2227eb6f7'})
	req.data=b'spravne'
	assert verify_signature(req)

def test_verify_wrong_signature(capsys):
	req = flexmock(requests.Request(), headers={'Signature': 'sha1=8dd7186bd499f38cfe5f3b829e9f931f105e760f'})
	req.data=b'neplatne'
	assert not verify_signature(req)

@pytest.fixture
def testapp():
    app = create_app(None)
    app.config['TESTING'] = True
    return app.test_client()

def test_list(testapp):
    assert 'event' in testapp.get('/list').get_data(as_text=True)

def test_add(testapp):
    JSON = '{"name": "JMENO", "when": "2220-01-30 19:25:00", "how": "mail", "message": "novej event", "subject": "predmet"}'
    rv = testapp.post('/add', json=json.loads(JSON), headers={'Signature': 'sha1=858bd13f8443a73bc62825451777faa52d7ca3ee'})

    assert rv.status_code == 200

def test_remove(testapp):
    JSON = '{"name": "JMENO", "when": "2220-01-30 19:25:00", "how": "mail", "message": "novej event", "subject": "predmet"}'
    ap = testapp
    rv = ap.post('/add', json=json.loads(JSON), headers={'Signature': 'sha1=858bd13f8443a73bc62825451777faa52d7ca3ee'})
    assert rv.status_code == 200  

    JSON = '{"id": "0"}'
    rv = ap.post('/remove', json=json.loads(JSON), headers={'Signature': 'sha1=a8bdd44c0eb374da291f9c5d2be444ace8d5b3b5'})
    assert rv.status_code == 200  


# def test_add_event(capsys):
# 	try:
# 		CREDENTIALS_FILE = os.environ['CREDENTIALS_FILE']
# 	except:
# 		CREDENTIALS_FILE = 'credentials.cfg'

# 	config = configparser.ConfigParser()
# 	with open(CREDENTIALS_FILE) as f:
# 		config.read_file(f)

# 	secret = config['web']['secret']

# 	sch = run_scheduler()
# 	JSON = '{"name": "JMENO", "when": "2020-01-30 19:25:00", "how": "mail", "message": "novej event", "subject": "predmet"}'

# 	mac = hmac.new(bytes(secret, encoding='ascii'), msg=bytes(JSON, encoding='ascii'), digestmod='sha1').hexdigest()

# 	p = requests.request(method = 'post', url='http://127.0.0.1:5000/add', json=json.loads(JSON), headers={"Signature": "sha1={}".format(mac)})
