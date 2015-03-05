from app import db # Get this app's DB object

# Want to make
# ------------------------
#          users
# ------------------------
# id      |  INTEGER   
# nickname|  VARCHAR(64)
# email   |  VARCHAR(120)
# ------------------------

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True) # Field is indexed
	email = db.Column(db.String(120), index=True, unique=True)

	def __repr__(self): # How to represent object
		return '<User %r>' % (self.nickname)