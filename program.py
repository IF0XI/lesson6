from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/poleshchuk')
def poleshchuk():
    return 'Hello from CI with GitHub Actions by Poleshchuk'
