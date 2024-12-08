from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
        
    def __repr__(self):
        return '<People %r>' % self.people

    def serialize(self):
        return {
            "id": self.id,
            "birth_year": self.birth_year,
            "eye_color" : self.eye_color,
            "gender" : self.gender,
            "skin_color" : self.skin_color,

        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
        
    def __repr__(self):
        return '<Planet %r>' % self.planet

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created" : self.created,
            "diameter" : self.diameter,
            "climate" : self.climate,

        }
    
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_capacity = db.Column(db.String(120), unique=False, nullable=False)
    consumables = db.Column(db.String(80), unique=False, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    model = db.Column(db.String(80), unique=False, nullable=False)
        
    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle

    def serialize(self):
        return {
            "id": self.id,
            "cargo_capacity": self.cargo_capacity,
            "consumables" : self.consumables,
            "created" : self.created,
            "model" : self.model,

        }
    


class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
    user = db.relationship(User)
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    people = db.relationship(People)
    planet_id = db.Column (db.Integer, db.ForeignKey("planet.id"))
    planet = db. relationship(Planet)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))
    vehicle = db.relationship(Vehicle)

        
    def __repr__(self):
        return '<Favoritos %r>' % self.favoritos
        

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id" : self.people_id,
            "planet_id" : self.planet_id,
            "vehicle_id" : self.vehicle_id,

        }
    

    

    
