from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

#initialize the flask application
app = Flask(__name__)

#disable the cross origin error pop up
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)




