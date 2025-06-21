
from flask import Flask,jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, Hero_Power


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


# Routes
@app.route('/')
def index():
   body = { "message": "Welcome to being a Hero"}
   return jsonify(body),200


# GET heroes
@app.route('/heroes')
def get_heroes():
    all_heroes = Hero.query.all()
    return jsonify([h.to_dict() for h in Hero.query.all()])


# GET /heroes/:id
@app.route('/heroes/<int:hero_id>')
def get_hero(hero_id):   
    hero = Hero.query.filter_by(id = hero_id).first()
    if hero:
        return jsonify(hero.to_dict()), 200
    else:
        return jsonify({ "error": "Hero not found" }), 404




# GET /powers
@app.route('/powers')
def get_powers():
    all_powers = Power.query.all()
    powers = jsonify([p.to_dict() for p in all_powers])
    return powers
    


# GET /powers/:id
@app.route('/power/<int:power_id>')
def get_power(power_id):
    power = Power.query.filter_by(id=power_id).first()
    if power:
        return jsonify(power.to_dict()), 200
    else:
        return jsonify({ "error": "Power not found"}), 404
    

# PATCH /powers/:id
@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_powers(power_id):
    power = Power.query.get(power_id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()

    try:
        new_description = data.get("description")
        if new_description:
            power.description = new_description
            db.session.commit()

        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["validation error", str(e)]}), 400



@app.route('/hero_powers', methods=['POST'])
def add_hero_powers():
    data = request.get_json()

    # Predefined strength options
    valid_strengths = ['Strong', 'Weak', 'Average']

    # Get hero and power
    hero = Hero.query.get(data.get('hero_id'))
    power = Power.query.get(data.get('power_id'))

    # Validations
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    if not power:
        return jsonify({"error": "Power not found"}), 404

    if data.get("strength") not in valid_strengths:
        return jsonify({"error": "Invalid strength value"}), 400

    try:
        hero_power = Hero_Power(
            strength=data.get("strength"),
            hero=hero, 
            power=power 
        )

        db.session.add(hero_power)
        db.session.commit()

        # Build full response dict manually
        result = {
            "id": hero_power.id,
            "strength": hero_power.strength,
            "hero_id": hero.id,
            "power_id": power.id,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description,
            }
        }

        return jsonify(result), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Validation error", str(e)]}), 400






if __name__ == '__main__':
    app.run(port=5555, debug=True)
