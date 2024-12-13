"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os, json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Vehicle, Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#GET

@app.route('/user', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        if len (users)<1:
            return jsonify({"msg": "not found"}), 404
        serialized_users = list(map(lambda x: x.serialize(),users))
        return serialized_users, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500
    
@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    try:
        user = User.query.get(user_id)
        if user is None :
            return jsonify({"msg": f"user {user_id} not found"}), 404
        serialize_user = user.serialize()
        return serialize_user, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500
    
@app.route('/user/favoritos/<int:user_id>', methods=['GET'])
def get_user_favoritos(user_id):
    try:
        favoritos = Favoritos.query.filter_by(user_id=user_id).all()
        if not favoritos:
            return jsonify({"msg": f"No favorites found for user {user_id}"}), 404
        return jsonify([fav.serialize() for fav in favoritos]), 200
    except Exception as e:
        return jsonify({"msg": "Server error", "error": str(e)}), 500

    

@app.route('/people', methods=['GET'])
def get_all_peoples():
    try:
        peoples = People.query.all()
        if len (peoples)<1:
            return jsonify({"msg": "not found"}), 404
        serialized_users = list(map(lambda x: x.serialize(),peoples))
        return serialized_users, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500
    
@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    try:
        people = People.query.get(people_id)
        if people is None :
            return jsonify({"msg": f"people{people_id}not found"}), 404
        serialized_user = people.serialize()
        return serialized_user, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500


@app.route('/planet', methods=['GET'])
def get_all_planets():
    try:
        planets = Planet.query.all()
        if len (planets)<1:
            return jsonify({"msg":"not found"}),404
        serialized_users = list(map(lambda x: x.serialize(),planets))
        return serialized_users, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500
    
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    try:
        planet = Planet.query.get(planet_id)
        if planet is None :
            return jsonify({"msg": f"planet{planet_id}not found"}), 404
        serialized_user = planet.serialize()
        return serialized_user, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500

    
@app.route('/vehicle', methods=['GET'])
def get_all_vehicles():
    try:
        vehicles = Vehicle.query.all()
        if len (vehicles)<1:
            return jsonify({"msg":"not found"}),404
        serialized_users = list (map(lambda x: x.serialize(),vehicles))
        return serialized_users, 200
    except Exception as e:
        return jsonify ({"msg":"server error", "error":str(e)}), 500
    
@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_one_vehicle(vehicle_id):
    try:
        vehicle = Vehicle.query.get(vehicle_id)
        if vehicle is None :
            return jsonify({"msg": f"planet{vehicle_id}not found"}), 404
        serialized_user = vehicle.serialize()
        return serialized_user, 200
    except Exception as e:
        return jsonify ({"msg":"Server error", "error":str(e)}), 500

    



    #POST

@app.route('/user',methods=['POST'])
def create_one_user():
    try:
        body=json.loads(request.data)
        new_user= User(
            email= body["email"],
            password= body["password"],
            is_active=True
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg":"User created succesfull"}),201
    except Exception as e:
        return jsonify({"msg":"server error","error":str(e)}), 500



@app.route('/people',methods=['POST'])
def create_one_people():
    try:
        body=json.loads(request.data)
        new_people= People(
            birth_year= body["birth_year"],
            eye_color= body["eye_color"],
            gender= body["gender"],
            skin_color= body["skin_color"]
        )
        db.session.add(new_people)
        db.session.commit()
        return jsonify({"msg":"People created succesfull"}),201
    except Exception as e:
        return jsonify({"msg":"server error","error":str(e)}), 500
    

@app.route('/planet',methods=['POST'])
def create_one_planet():
    try:
        body=json.loads(request.data)
        new_planet= Planet(
            name= body["name"],
            created= body["created"],
            diameter= body["diameter"],
            climate= body["climate"]
        )
        db.session.add(new_planet)
        db.session.commit()
        return jsonify({"msg":"Planet created succesfull"}),201
    except Exception as e:
        return jsonify({"msg":"server error","error":str(e)}), 500


@app.route('/vehicle',methods=['POST'])
def create_one_vehicle():
    try:
        body=json.loads(request.data)
        new_vehicle= Vehicle(
            cargo_capacity= body["cargo_capacity"],
            consumables= body["consumables"],
            created= body["created"],
            model= body["model"]
        )
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify({"msg":"Vehicle created succesfull"}),201
    except Exception as e:
        return jsonify({"msg":"server error","error":str(e)}), 500
    

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    try:
        user_id = 3
        user = User.query.get(user_id)
        if not user:
            return jsonify({"msg": "User not found"}), 404
        planet = Planet.query.get(planet_id)
        if not planet:
            return jsonify({"msg": "Planet not found"}), 404
        existing_favorite = Favoritos.query.filter_by(user_id=user_id, planet_id=planet_id).first()
        if existing_favorite:
            return jsonify({"msg": "Planet is already in favorites"}), 400
        new_favorite = Favoritos(
            user_id=user_id,
            planet_id=planet_id
        )
        db.session.add(new_favorite)
        db.session.commit()
        
        return jsonify({"msg": "Planet added to favorites successfully"}), 201
    except Exception as e:
        return jsonify({"msg": "Server error", "error": str(e)}), 500
   

#

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
