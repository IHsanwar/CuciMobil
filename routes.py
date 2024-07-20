from main import app, send_from_directory, render_template

from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from peewee import SqliteDatabase
from model.Login import *
from model.Form import LoginForm, RegisterForm 
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/success", methods=["GET"])
def success():
    return render_template('success.html' )

@app.route("/blankplain", methods=["GET"])
def form_loading():
    return 'Loading...'


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static/assets', path)


@app.route("/", methods=["GET"])
def home():
    # ret = {"status": 1, "body": "Test"}
    return render_template('index.html')


