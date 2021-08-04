from connect import *


class Operator(Model):
    id = IntegerField()
    code = CharField()
    name = CharField()
    phone = CharField()
    fee = IntegerField()

    class Meta:
        database = db

