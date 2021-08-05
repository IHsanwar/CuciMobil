from connect import *


class Services(Model):
    id = IntegerField()
    code = CharField()
    name = CharField()
    price = IntegerField()
    many_operators = IntegerField()
    created_on = CharField()

    class Meta:
        database = db