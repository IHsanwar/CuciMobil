from connect import *


class Operators(Model):
    id = IntegerField()
    code = CharField()
    name = CharField()
    phone = CharField()
    fee = IntegerField()

    class Meta:
        database = db

