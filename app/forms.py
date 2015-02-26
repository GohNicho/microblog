from flask.ext.wtf import form 					# Uses form from flask-wtf
from wtforms import StringField, BooleanField	# String for the OpenID, Boolean for remember me
from wtforms.validators import DataRequired 	# Included to validate that is not empty

class LoginForm(Form):
	openid = StringField('openid', validators =[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)