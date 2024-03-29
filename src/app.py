from flask import Flask

app = Flask(__name__)
@app.route('/')

def say_something():
    return '<h1>What is wrong with the leaders of today?</h1>'

if __name__ == '__main__':
    app.run()
