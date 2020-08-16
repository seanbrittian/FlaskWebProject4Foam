"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, Blueprint
#from FoamProject import auth as auth_blueprint, main


#from FlaskWebProject4 import models





app = Flask(__name__, template_folder="templates")
db = SQLAlchemy(app)
#app.config['SECRET_KEY'] = 'Administrator'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SQLiteToolTracker3.db'
#db.init_app(app)

#from auth import auth as auth_blueprint
#from auth import auth as auth_blueprint
#app.register_blueprint(auth_blueprint)

#from ProjectFoam.FoamProject import main as main_blueprint
#app.register_blueprint(main_blueprint)

#db.init_app(app)
class Tools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_code = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    tool_num = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    c520 = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    last_heat = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    prod_days = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    enter_wipe = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    enter_blasting = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)


def __init__(tools, id, tool_code, tool_num, C520, last_heat, prod_days, enter_wipe, enter_blasting):
    tools.id = tools
    tools.tool_code = tool_code
    tools.tool_num = tool_num
    tools.C520 = C520
    tools.last_heat = last_heat
    tools.prod_days = prod_days
    tools.enter_wipe = enter_wipe
    tools.enter_blasting = enter_blasting

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    level = db.Column(db.Integer)
    logged = db.Column(db.Integer)

def __init__(users, id, name, level):
    users.id= id
    users.name= name
    users.level = level
    users.logged = logged


db.create_all()




# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#from ..models import Tools

@app.route('/')
def home():
   return render_template('/home.html',  Tools = Tools.query.all())

@app.route('/show_all')
def show_all():
   return render_template('/show_all.html',  Tools = Tools.query.all() )




if __name__ == '__main__':
    
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #db.create_all()
    app.run(HOST, PORT)