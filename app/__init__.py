from flask import Flask, request, jsonify
from flask import render_template
from flask_script import Manager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

CORS(app)
app.config.from_object('config')
db  = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Registers(db.Model):
    __tablename__ = "registers"

    id = db.Column(db.BigInteger, primary_key=True)
    ip = db.Column(db.String(255), nullable=True)
    x_coord = db.Column(db.String(255), nullable=True)
    y_coord = db.Column(db.String(255), nullable=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, ip, x_coord, y_coord):
        self.ip = ip
        self.x_coord = x_coord
        self.y_coord = y_coord

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<register %r>" % self.ip


@app.route('/')
def initial_page():
    return render_template('home.html')

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("X: {}, Y: {}, IP: {}\n".format(data['x_coord'], data['y_coord'], data['ip']))
    sys.stdout.flush()

    obj = Registers(ip=data['ip'], x_coord=data['x_coord'], y_coord=data['y_coord'])
    db.session.add(obj)
    db.session.commit()    
        
    return jsonify({"success": True})