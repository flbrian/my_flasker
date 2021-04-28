'''
################################################################
This is the Edit Golf Round Window for the Golf Tracking Program
Created: 03/24/2021
Updated: 03/30/2021
Author:  Brian Greenberg
################################################################
'''

from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

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







