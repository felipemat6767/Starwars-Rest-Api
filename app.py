import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Character, Planets, Starships, Favorites, FavoriteCharacter, FavoritePlanet, Favoriteship
from flask_migrate import Migrate


Basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(Basedir, "test.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["ENV"] = "developement"
app.config["Debug"] = True

Migrate(app, db)
db.init_app(app)

@app.route("/")
def Home():
  return jsonify("H")


@app.route("/user", methods = ["POST", "GET"])
def user():
    if request.method == "GET":
        users = User.query.all()
        if users is None:
            return jsonify(error = "Usuario No encontrado"), 400
        results = list(map(lambda users: users.serialize(), users))
        return jsonify(results)
    
    if request.method == "POST":
        user = User()
        user.name = request.json.get("name")
        user.email = request.json.get("email")
        
        if user.name == "":
             return jsonify(error = "Falta informacion"), 400
        if user.email == "":
            return jsonify(error = "Falta informacion"), 400
        
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize()), 200
    
@app.route("/user/<int:id>", methods = ["GET", "DELETE"])
def userid(id = None):
  if request.method == "GET":
        user = User.query.get(id)
        if user is None:
            return jsonify(error = "Usuario No encontrado"), 400
        return jsonify(user.serialize())

  if request.method == "DELETE":
        deleted_users = User.query.filter_by(id = id).first()
        if deleted_users is not None:
            db.session.delete(deleted_users)
            db.session.commit() 
            return jsonify(deleted_users.serialize_username())
        
        db.session.remove(deleted_users)
        db.session.commit()
        return jsonify(deleted_users.serialize()), 200


@app.route("/characters", methods = ["POST", "GET"])
def characters():
    if request.method == "GET":
        characters = Character.query.all()
        if characters is None:
            return jsonify(error = "Usuario No encontrado"), 400
        results = list(map(lambda characters: characters.serialize(), characters))
        return jsonify(results)
    
    if request.method == "POST":
        characters = Character()
        characters.name = request.json.get("name")
        characters.gender = request.json.get("gender")
        characters.homeworld = request.json.get("homeworld")
        
        if characters.name == "":
             return jsonify(error = "Falta informacion"), 400
        if characters.gender == "":
            return jsonify(error = "Falta informacion"), 400
        if characters.homeworld == "":
            return jsonify(error = "Falta informacion"), 400
        
        db.session.add(characters)
        db.session.commit()
        return jsonify(characters.serialize()), 200
    
@app.route("/characters/<int:id>", methods = ["POST", "GET", "DELETE"])
def character(id):
    if request.method == "GET":
        character = Character.query.get(id)
        if character is not None:
            return jsonify(character.serialize_username())

    if request.method == "DELETE":
        deleted_characters = Character.query.filter_by(id = id).first()
        if deleted_characters is not None:
            db.session.delete(deleted_characters)
            db.session.commit() 
            return jsonify(deleted_characters.serialize_username())     
        
@app.route("/planets", methods = ["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planets.query.all()
        if planets is None:
            return jsonify(error = "Usuario No encontrado"), 400
        results = list(map(lambda planets: planets.serialize(), planets))
        return jsonify(results)
    
    if request.method == "POST":
        planets = Planets()
        planets.name = request.json.get("name")
        planets.population = request.json.get("population")
       
        if planets.name == "":
             return jsonify(error = "Falta informacion"), 400
        if planets.population == "":
            return jsonify(error = "Falta informacion"), 400
        
        db.session.add(planets)
        db.session.commit()
        return jsonify(planets.serialize()), 200
    
@app.route("/planets/<int:id>", methods = ["GET", "DELETE"])
def planetsid(id = None):
  if request.method == "GET":
        planets = Planets.query.get(id)
        if planets is not None:
            return jsonify(planets.serialize())

  if request.method == "DELETE":
        deleted_planets = Planets.query.filter_by(id = id).first()
        if deleted_planets is not None:
            db.session.delete(deleted_planets)
            db.session.commit() 
            return jsonify(deleted_planets.serialize())     

@app.route("/starships", methods = ["POST", "GET"])
def starships():
    if request.method == "GET":
        starships = Starships.query.all()
        if starships is None:
            return jsonify(error = "Usuario No encontrado"), 400
        results = list(map(lambda starships: characters.serialize(), starships))
        return jsonify(results)
    
    if request.method == "POST":
        starships= Starships()
        starships.name = request.json.get("name")
        starships.model = request.json.get("model")
       
        if starships.name == "":
             return jsonify(error = "Falta informacion"), 400
        if starships.model == "":
            return jsonify(error = "Falta informacion"), 400
        
        db.session.add(starships)
        db.session.commit()
        return jsonify(starships.serialize()), 200
    
@app.route("/starships/<int:id>", methods = ["POST", "GET", "DELETE"])
def starshipsid(id):
  if request.method == "GET":
        starships = Starships.query.get()
        if starships is not None:
            return jsonify(starships.serialize())

  if request.method == "DELETE":
        deleted_starships = Starships.query.filter_by(id = id).first()
        if deleted_starships is not None:
            db.session.delete(deleted_starships)
            db.session.commit() 
            return jsonify(deleted_starships.serialize())     


@app.route("/favorites", methods = ["POST", "GET"])
def favorites ():
    if request.method == "POST":
        favorites = Favorites()
        favorites.user_id = request.json.get("user_id")
        favorites.planet_name= request.json.get("planet_name")
        favorites.character_name= request.json.get("character_name")
        db.session.add(favorites)
        db.session.commit()
        return jsonify(success = "Agregado a favoritos"), 200
    
    if request.method == "GET":
        if id is not None:
            user_favorites = Favorites.query.all()
            if user_favorites is None:
                return jsonify(error ="No se encontro usuario"), 404 
            return jsonify(list(map(lambda x: x.serialize(), user_favorites)))
    
@app.route("/favorites/<int:id>", methods = ["GET", "DELETE", "POST"])
def favoritesid(id = None):
    if request.method == "GET":
       if id is not None:
            user_favorites = Favorites.query.filter_by(user_id = id)
            if user_favorites is None:
                return jsonify(error ="No se encontro usuario"), 404 
            return jsonify(list(map(lambda x: x.serialize(), user_favorites)))

    if request.method == "DELETE":
        deleted_favorites = Favorites.query.filter_by(id = id).first()
        if deleted_favorites is not None:
            db.session.delete(deleted_favorites)
            db.session.commit() 
            return jsonify(deleted_favorites.serialize_username())    
         
  
    

@app.route("/favorites/favorite_planet/<int:id>", methods = ["POST", "GET", "DELETE"])
def favorite_planet(id = None):
    if request.method == "GET":
       if id is not None:
            user = User.query.get(id)
            if user is None:
                return jsonify(error ="No se encontro usuario"), 404 
            return jsonify(list(map(lambda favorite: favorite.serialize(), user.favorites)))

    if request.method == "DELETE":
        deleted_favorites = Favorites.query.filter_by(id = id).first()
        if deleted_favorites is not None:
            db.session.delete(deleted_favorites)
            db.session.commit() 
            return jsonify(deleted_favorites.serialize())     
    
    if request.method == "POST":
        favorites = Favorites()
        favorites.user_id = request.json.get("user_id")
        favorites.planet_name = request.json.get("planet_name")
        db.session.add(favorites)
        db.session.commit()
        return jsonify(success = "Creado Exitosamente"), 200

@app.route("/favorites/favorite_starships/<int:id>", methods = ["POST", "GET", "DELETE"])
def favorite_starships(id = None):
    if request.method == "GET":
       if id is not None:
            user = User.query.get(id)
            if user is None:
                return jsonify(error ="No se encontro usuario"), 404 
            return jsonify(list(map(lambda favorite: favorite.serialize(), user.favorites)))

    if request.method == "DELETE":
        deleted_favorites = Favorites.query.filter_by(id = id).first()
        if deleted_favorites is not None:
            db.session.delete(deleted_favorites)
            db.session.commit() 
            return jsonify(deleted_favorites.serialize())     
    
    if request.method == "POST":
        favorites = Favorites()
        favorites.user_id = request.json.get("user_id")
        favorites.starship_name = request.json.get("starship_name")
        db.session.add(favorites)
        db.session.commit()
        return jsonify(success = "Creado Exitosamente"), 200
    
@app.route("/favorites/favorite_character/<int:id>", methods = ["POST", "GET", "DELETE"])
def favorite_character(id = None):
    if request.method == "GET":
       if id is not None:
            user = User.query.get(id)
            if user is None:
                return jsonify(error ="No se encontro usuario"), 404 
            return jsonify(list(map(lambda favorite: favorite.serialize(), user.favorites)))

    if request.method == "DELETE":
        deleted_favorites = Favorites.query.filter_by(id = id).first()
        if deleted_favorites is not None:
            db.session.delete(deleted_favorites)
            db.session.commit() 
            return jsonify(deleted_favorites.serialize())     
    
    if request.method == "POST":
        favorites = Favorites()
        favorites.user_id = request.json.get("user_id")
        favorites.character_name = request.json.get("character_name")
        db.session.add(favorites)
        db.session.commit()
        return jsonify(success = "Creado Exitosamente"), 200
    
if __name__ == "__main__":
    app.run(host ="localhost", port = 5080)
