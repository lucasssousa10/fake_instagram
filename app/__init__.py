from flask import Flask, request, jsonify
from flask import render_template
from flask_script import Manager
from flask_cors import CORS
import sys

app = Flask(__name__)

CORS(app)
manager = Manager(app)

@app.route('/')
def initial_page():
    return render_template('home.html')

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("X: {}, Y: {}, IP: {}\n".format(data['x_coord'], data['y_coord'], data['ip']))
    sys.stdout.flush()
    
    fo= open("results.txt", "a")
    filebuffer = ["X: {}, Y: {}, IP: {}\n".format(data['x_coord'], data['y_coord'], data['ip'])]
    fo.writelines(filebuffer)
    fo.close()

    
    
    return jsonify({"success": True})