from flask_sqlalchemy import SQLAlchemy
from api_to_interact_with_bank_db import app

# this will config the sqlite3 database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
db = SQLAlchemy(app)


# this will create the table that will hold the records
# it also defines the parameters for the fields that will be
# ...holding the values for each record

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(100), nullable=False)
	lname = db.Column(db.String(100), nullable=False)
	chk_bal = db.Column(db.Integer, nullable=False)

	# this create a user-friendly string that will display to describe
	# ...a record from the database if it is called via code
	# def __repr__(self):
	# 	return f"member(name = {name}, views = {views}, likes = {likes})"

# YOU NEED TO RUN THE FUNCTION TO CREATE THE DATABASE!!!!!!!
# comment this line after the database has been created
# uncomment this line to create a new empty databse
# db.create_all()




