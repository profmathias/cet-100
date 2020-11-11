from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return f'Hi...'


def main():
    print('App started...')
    app.run(host='0.0.0.0')
