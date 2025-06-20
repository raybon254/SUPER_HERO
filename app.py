
from flask import Flask, make_response
from flask_migrate import Migrate
from models.conn import db
import json, requests

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


# Routes
@app.route('/')
def index():
   body = { "message": "Welcome to this trial page"}
   return make_response(body,200)


# GET heroes
@app.route('/')
def index():
    pass


# GET /heroes/:id
@app.route('/heroes/<int:id>')
def get_hero(hero_id):
    pass

# GET /powers
@app.route('/<powers>')
def get_powers(power):
    pass


# GET /powers/:id
@app.route('/powers/<int:id>')
def get_power(power):
    pass

# PATCH /powers/:id
@app.route('/powers/<int:id>')
def update_powers(power):
    pass

# POST /hero_powers
@app.route('/powers/<int:id>')
def add_hero_powers():
    pass





if __name__ == '__main__':
    app.run(port=5555, debug=True)

clea