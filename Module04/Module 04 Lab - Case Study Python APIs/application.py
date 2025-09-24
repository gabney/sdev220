"""
Module 04 Lab - Case Study: Python APIs
SDEV 220 Software Development Using Python
Gabriel Abney

This assignment recreates the REST API tutorial found in the 
video at https://www.youtube.com/watch?v=qbLc5a9jdXo.

This requires using pip to install the libraries 'flask' and 'flask-sqlalchemy'.
"""


#imports Flask library
from flask import Flask

# imports sqlalchemy to handle database manipulation
from flask_sqlalchemy import SQLAlchemy

# sets the Flask app variable to this file
app = Flask(__name__)


# creates dat.db in the directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# sets the database to be db
db = SQLAlchemy(app)




# class to store the items in the database
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"



# sets up the routing for the API main directory
@app.route("/")
# sets return statement for accessin
def testing_api():
    return "<h1>Hello!</h1>"

# sets up drink director
@app.route("/drinks")
def get_drinks():
    return {"drinks":"drink data"}

#runs the Flask app with debugging turned on
app.run(debug=True)