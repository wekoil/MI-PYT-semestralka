from flask import Flask, render_template, request

import flask

from scheduler import Scheduler

import hmac

app = Flask(__name__)

def run_scheduler():
    """Loads calendar and stars scheduler"""
    sch = Scheduler()
    sch.load_calendar('my.ics')

    sch.run()
    return sch

sch = run_scheduler()


blueprint = flask.Blueprint('my', __name__)

def verify_signature(req):
    """Verify signature of request"""
    secret = '1234'

    if secret == None:
        return True

    header_signature = req.headers.get('Signature')
    
    print(header_signature)

    if header_signature == None:
        return False

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return False

    print(req.data)

    mac = hmac.new(bytes(secret, encoding='ascii'), msg=req.data, digestmod='sha1').hexdigest()
    print(mac)
    if not str(mac) == str(signature):
        return False
    return True

@blueprint.route('/list')
def list():
    """Lists all events."""

    events = sch.get_events()
    return render_template('index.html', events=events)


@app.route('/add', methods=['POST'])
def add_event():
    """Adds event to scheduler."""
    for atr in ['name', 'when', 'how']:
        if atr not in request.get_json():
            abort(400)
    
    if not verify_signature(request):
        abort(400)

    json = request.get_json()
    event = Scheduler.create_event(name=json.get('name'), when=json.get('when'), how=json.get('how'),  receiver=json.get('receiver'), message=json.get('message'), subject=json.get('subject'))
    sch.process_event(event)

    return '', 200

@app.route('/remove', methods=['POST'])
def remove_event():
    """Removes event from scheduler with specified id."""
    if 'id' not in request.get_json():
        abort(400)
    
    if not verify_signature(request):
        abort(400)

    json = request.get_json()
    sch.remove_event(event_id=json.get('id'))

    return '', 200


if __name__ == '__main__':
    app.register_blueprint(blueprint)
    app.run(debug=True,use_reloader=True)
