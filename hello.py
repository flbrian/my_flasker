'''
################################################################
This is my main module of the Flask Program
Created: 04/24/2021
Updated: 04/30/2021
Author:  Brian Greenberg
################################################################
'''

from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a flask instance
app = Flask(__name__)


# Add database and point to one we want to use
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:SQL1viera2X!@localhost/our_users'

# Old db using sqlite
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'


# Add secret key!
app.config['SECRET_KEY']="mysuperscretkey"

# initialize the database
db = SQLAlchemy(app)

# Create a model
class Users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(60), nullable = False)
	email = db.Column(db.String(120), nullable = False)
	date_added = db.Column(db.DateTime, default = datetime.utcnow)

	# Create a string
	def __repr__(self):
		return '<Name %r>' % self.name

# Create a form
class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a form
class NamerForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	submit = SubmitField("Submit")

	# Here is a list of possible field validators!

	# BooleanField
	# DateField
	# DateTimeField
	# DecimalField
	# FileField
	# HiddenField
	# MultipleField
	# FieldList
	# FloatField
	# FormField
	# IntegerField
	# PasswordField
	# RadioField
	# SelectField
	# SelectMultipleField
	# SubmitField
	# StringField
	# TextAreaField

	# Here is a list of other validators!

	# DataRequired
	# Email
	# EqualTo
	# InputRequired
	# IPAddress
	# Length
	# MacAddress
	# NumberRange
	# Optional
	# Regexp
	# URL
	# UUID
	# AnyOf
	# NoneOf

# FOLLOWING will allow us to add a user
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
	# Start with name and email as blanks and throw up the entry form
	name = None
	email = None
	form = UserForm()

	# make sure all required data was entered on the form
	if form.validate_on_submit():
		# Check whether email address entered already exists
		user = Users.query.filter_by(email = form.email.data).first()
		if user is None:
			# Email entered does not exist in the database - ok to add user
			user = Users(name = form.name.data, email = form.email.data)
			db.session.add(user)
			db.session.commit()
			flash("New user added successfully")
		else:
			flash("User already exists - Not added again!")
	name = form.name.data
	form.name.data = ''
	form.email.data = ''
	
	# Get most current list of users
	our_users = Users.query.order_by(Users.date_added)

	return render_template("add_user.html", 
		form=form,
		name=name,
		our_users=our_users)


# Create a route (decorator) for the index page
@app.route('/')

# Now, defind the index web page
def index():
	favorite_colors = ["blue", "white", "purple"]
	return render_template("index.html",
		favorite_colors=favorite_colors)

# Create a route (decorator) for the user page
@app.route('/user/<name>')

# Define the user web page
def user(name):
	return render_template("user.html", user_name=name)

# Deal with URL not found - 404 error
@app.errorhandler(404)
def Page_Not_Found(e):
	return render_template("404.html"), 404

# Deal with internal server problem - 500 error
@app.errorhandler(500)
def Internal_Server_Error(e):
	return render_template("500.html"), 500

# Create a route (decorator) for the Name page
@app.route('/name' , methods=['GET', 'POST'])

# Define the Name web page
def name():
	name=None
	form = NamerForm()


	# validate the name
	if form.validate_on_submit():
		name = form.name.data 
		form.name.data = ''
		flash("Form submitted successfully!")
		
	return render_template("name.html",
		name = name,
		form = form)







