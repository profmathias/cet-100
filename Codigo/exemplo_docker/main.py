from flask import Flask

app = Flask(__name__)


@app.route('/greetings')
def print_hi():
    return 'Hi, mathias'


def main():
    app.run('127.0.0.1', '5000')
