from flask import Flask, jsonify, render_template, request
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
from random import choice
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
TopSecretAPIKey=os.environ['API_KEY']
# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random",methods=["GET"])
def random():
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
        random_cafe = choice(all_cafes)
        return jsonify(cafe={
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "amenities": {
                "seats": random_cafe.seats,
                "has_toilet": random_cafe.has_toilet,
                "has_wifi": random_cafe.has_wifi,
                "has_sockets": random_cafe.has_sockets,
                "can_take_calls": random_cafe.can_take_calls,
                "coffee_price": random_cafe.coffee_price,
            }
        })

@app.route("/all")
def get_all():
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        all_cafes = result.scalars().all()
        # Convert objects to dictionaries
        cafes_list = [cafe.__dict__ for cafe in all_cafes]

        # Remove SQLAlchemy internal state
        for cafe in cafes_list:
            cafe.pop('_sa_instance_state', None)

        # Create the final dictionary
        cafes_dict = {"cafes": cafes_list}

        # Return as JSON
        return jsonify(cafes=cafes_dict)

@app.route("/search")
def search():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    # Note, this may get more than one cafe per location
    all_cafes = result.scalars().all()
    cafes_list = [cafe.__dict__ for cafe in all_cafes]
    for cafe in cafes_list:
        cafe.pop('_sa_instance_state', None)
    cafes_dict = {"cafes": cafes_list}
    if cafes_dict:
        return jsonify(cafes=cafes_dict)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def remove_cafe(cafe_id):
     in_api_key = request.args.get("api-key")
     if in_api_key==TopSecretAPIKey:
         try:
             cafe = db.get_or_404(Cafe, cafe_id)
         except AttributeError:
             return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
         else:
             db.session.delete(cafe)
             db.session.commit()
         return jsonify(response={"success": "Successfully updated the price."}), 200
     elif in_api_key!=TopSecretAPIKey:
         return jsonify(Forbidden={ "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
     else:
         return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}),404


if __name__ == '__main__':
    app.run(debug=True,port=8080)
