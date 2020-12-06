from flask import Flask, request, abort
import datetime
import time
import json


db = [
    {
        'name': 'Jack',
        'text': 'Hello everyone!',
        'time': time.time()
    }, {
        'name': 'Marry',
        'text': 'Hello Jack!',
        'time': time.time()
    }
]

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'StrongBody',
        'time': datetime.datetime.now(),
        'users_count': len(set(n['name'] for n in db)),
        'messages_count': len(db)
        # "time": datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        # "time": time.strftime("%Y/%m/%d %H:%M")
        # "time": time.strftime("%x %X", time.localtime())
           }




@app.route("/send", methods=['POST'])
def send_message():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not (isinstance(name, str)
            and isinstance(text, str)
            and name
            and text):
        return abort(400)

    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)

    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args.get('after', 0))
    except ValueError:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {'messages': messages}


app.run()
