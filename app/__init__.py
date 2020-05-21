from flask import Flask
from flask_script import Manager
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
manager = Manager(app)

@app.route('/')
def hello_world():
    return 'Olá meu bovino...'
