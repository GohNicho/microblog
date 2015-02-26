from flask import render_template
from app import app

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
