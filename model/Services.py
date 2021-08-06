from .connect import *


class Servs(Model):
    id = IntegerField(primary_key=True)
    code = CharField()
    name = CharField()
    price = IntegerField()
    many_operators = IntegerField()
    created_on = CharField()

    class Meta:
        database = db
        db_table = 'services'