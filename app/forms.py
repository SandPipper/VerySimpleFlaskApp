from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from .models import Person

class Add_personForm(FlaskForm):

    first_name = StringField('first_name', validators=[DataRequired(),
                                Length(min=2, max=16)])
    surname = StringField('surname', validators=[DataRequired(),
                                Length(min=2, max=20)])
