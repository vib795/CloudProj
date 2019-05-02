from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
	name = StringField('Name', validators=[Length(min=2, max=100)])
	address = StringField('Address', validators=[Length(min=5, max=100)])
	state = StringField('State', validators=[Length(min=3, max=20)])
	submit = SubmitField('Search')