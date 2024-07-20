from peewee import Model, CharField, SqliteDatabase
from flask_login import UserMixin
from .connect import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class User(UserMixin, Model):
    username = CharField(unique=True)
    password = CharField()
    id_user = IntegerField(primary_key=True)
    
    class Meta:
        database = db
        db_table = 'user'

        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')
