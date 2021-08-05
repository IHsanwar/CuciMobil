from .connect import *


class Customers(Model):
    id = IntegerField()
    nopol = CharField()
    owner = CharField()
    phone = CharField()
    vehicle_model = IntegerField()
    created_on = CharField()

    class Meta:
        database = db

