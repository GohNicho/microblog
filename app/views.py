from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/') # Links these two URLs to this view
@app.route('/index')

def index():
	user = {'nickname': 'Windy'} # placeholder user

	# Begin fake post array
	posts = [ 
		{
			'author': {'nickname': 'Nick'},
			'body': 'My first Flask thingy'
		},
		{
			'author': {'nickname': 'Windy'},
			'body': 'I love PSL305 <3333'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])

def login():
	form = LoginForm()							# Use LoginForm (from forms.py)
	if form.validate_on_submit():				# Validates forms, returns false if user has not entered data
		flash('Login requested for OpenID="%s", remember_me=%s' %  # Flash provides sorta error
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')				# Redirect points to another page (after flash)
	return render_template('login.html',		# Render this template
							title='Sign In',	# Pass this title in
							form=form,			# Let form be this form
							providers=app.config['OPENID_PROVIDERS'])	# Gets provider list from config		