from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#from app.models import User

class InputForm(FlaskForm):
	area=StringField('Area', validators=[DataRequired()])
	loc=StringField('Location', validators=[DataRequired()])
	sqft=StringField('sq-ft', validators=[DataRequired()])
	bath=StringField('Bathroom', validators=[DataRequired()])
	balcony=StringField('Balcony', validators=[DataRequired()])
	bhk=StringField('BHK', validators=[DataRequired()])
	submit = SubmitField('Predict price')