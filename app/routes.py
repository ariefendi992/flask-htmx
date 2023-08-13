from flask import Blueprint, render_template, request, jsonify
from .forms import LocationForm
from .models import City

main = Blueprint("main", __name__)


@main.route("/", methods=["POST", "GET"])
def index():
    form = LocationForm()
    if form.country.data:
        form.city.query = City.query.filter_by(country_id=form.country.data.id).all()
    else:
        form.city.query = City.query.filter(None).all()

    if form.validate_on_submit():
        print(form.country.data.name)
        print(form.city.data.name)
    return render_template("index.html", form=form)


@main.route("/get-cities")
def get_city():
    country_id = request.args.get("country", type=int)
    cities = City.query.filter_by(country_id=country_id).all()

    # return render_template("city_option.html", cities=cities)
    return [f'<option value={city.id}>{city.name}</option>"' for city in cities]
