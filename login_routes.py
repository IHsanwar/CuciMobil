from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from peewee import SqliteDatabase
from models import User
from forms import LoginForm, RegisterForm

