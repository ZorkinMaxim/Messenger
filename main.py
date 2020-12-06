import time
import datetime

# name = input('Input the name: ')
# print('Hello, ' + name)

message1 = {
    'name': 'Jack',
    'text': 'Hello everyone!',
    'time': time.time()
}

message2 = {
    'name': 'Marry',
    'text': 'Hello Jack!',
    'time': time.time()
}

db = [message1, message2]


def send_message(name, text):
    new_message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(new_message)


def get_messages(after=0):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


def print_messages(messages):
    for message in messages:
        beauty_time = datetime.datetime.fromtimestamp(message['time'])
        beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M')
        print(beauty_time, message['name'])
        print(message['text'])
        print()


send_message('A', '123')
get_messages()
print_messages(get_messages())
