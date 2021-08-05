from model.Services import *
from main import request
from random import randint
import datetime


class ServicesController(object):
    @staticmethod
    def list_services():
        return Services.select()
