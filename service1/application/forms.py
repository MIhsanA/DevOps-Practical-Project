from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from application.models import Person


class PersonForm(FlaskForm):
    name = StringField('Name',
            validators = [
                DataRequired(),
                Length(min=2, max=100)
            ]
    )
    submit = SubmitField('Enter')

