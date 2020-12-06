from PyQt5 import QtWidgets, QtCore
import clientui
import requests
from datetime import datetime


class Window(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def get_messages(self):
        try:
            response = requests.get('http://127.0.0.1:5000/messages',
                                    params={'after': self.after})
        except:
            return

        response.data = response.json()  # {'messages': messages}

        for message in response.data['messages']:
            self.print_message(message)
            self.after = message['time']

    def print_message(self, message):
        beauty_time = datetime.fromtimestamp(message['time'])
        beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M')
        self.textBrowser.append(beauty_time + ' ' + message['name'])
        self.textBrowser.append(message['text'])
        self.textBrowser.append('')

    def send_message(self):
        name = self.lineEdit.text()
        text = self.plainTextEdit.toPlainText()
        print(text)

        try:
            response = requests.post('http://127.0.0.1:5000/send', json={
                'name': name,
                'text': text
            })
        except:
            self.textBrowser.append('The server is temporarily unavailable')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append("Name or Text isn't filled")
            self.textBrowser.append('')
            return

        self.plainTextEdit.clear()


app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec_()
