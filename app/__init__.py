from flask import Flask
from .routes import main
from .extensions import db
from .models import Country, City
from settings import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main)
    db.init_app(app)

    return app


app = create_app()


def add_data():
    app.app_context().push()
    db.create_all()

    us = Country(name="United States")
    ca = Country(name="Canada")
    mx = Country(name="Mexico")
    id = Country(name="Indonesia")

    db.session.add_all([us, ca, mx, id])

    db.session.add_all(
        [
            City(name="New York", country=us),
            City(name="Los Angeles", country=us),
            City(name="Chicago", country=us),
            City(name="Toronto", country=ca),
            City(name="Montreal", country=ca),
            City(name="Vancouver", country=ca),
            City(name="Mexico City", country=mx),
            City(name="Guadalajara", country=mx),
            City(name="Monterrey", country=mx),
            City(name="Jakarta", country=id),
            City(name="Bali", country=id),
            City(name="Makassar", country=id),
        ]
    )

    db.session.commit()
