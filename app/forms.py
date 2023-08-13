from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from .models import Country


class LocationForm(FlaskForm):
    attr = {"hx-get": "/get-cities", "hx-target": "#city"}
    country = QuerySelectField(
        "Country",
        query_factory=lambda: Country.query.all(),
        allow_blank=True,
        blank_text="-Pilih-",
        get_label="name",
        render_kw=attr,
    )
    city = QuerySelectField("City", get_label="name", allow_blank=True)
