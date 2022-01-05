from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    favorites = db.relationship("Favorites", backref="user")
    
    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }

class Character (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    gender = db.Column(db.String(20), nullable = False)
    homeworld = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "homeworld": self.homeworld
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }

class Planets (db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    population = db.Column(db.String(20), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   
    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }

class Starships (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    model = db.Column(db.String(10), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model
        }

class Films (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Films %r>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "title": self.title,
            "episode_id": self.episode_id,
            "opening_crawl": self.opening_crawl,
            "director": self.director,
            "producer": self.producer,
            "release_date": self.release_date,
            "characters": self.characters,
            "planets": self.planets,
            "starships": self.starships,
            "vehicles": self.vehicles,
            "species": self.species,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
        }


class Favorites (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_name = db.Column(db.String(200))
    character_name = db.Column(db.String(200))

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_name": self.planet_name,
            "character_name": self.character_name
        }

    def serialize_username(self): 
        return {
            "id": self.id,
        }
        
class FavoritePlanet (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(200))
    favorites_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))


    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "planet_name": self.planet_name
        }

    def serialize_username(self): 
        return {
            "id": self.id,
        }
        
class FavoriteCharacter (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(200))
    favorites_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "character_name": self.character_name
        }

    def serialize_username(self): 
        return {
            "id": self.id,
        }
        
class Favoriteship (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starship_name = db.Column(db.String(200))
    favorites_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "starship_name": self.starship_name
        }

    def serialize_username(self): 
        return {
            "id": self.id,
        }