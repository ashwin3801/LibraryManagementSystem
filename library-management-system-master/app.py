from flask import Flask, g, escape, session, redirect, render_template, request, jsonify, Response
from Misc.functions import *

app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

# Setting DAO Class
from Models.DAO import DAO

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='password123'
app.config['MYSQL_DB']='lms'
app.config['MYSQL_CURSORCLASS']='DictCursor'


DAO = DAO(app)

# Registering blueprints
from routes.user import user_view
from routes.book import book_view
from routes.admin import admin_view

# Registering custom functions to be used within templates
app.jinja_env.globals.update(
    ago=ago,
    str=str,
)

app.register_blueprint(user_view)
app.register_blueprint(book_view)
app.register_blueprint(admin_view)