from .connect import *


class Operators(Model):
    id = IntegerField(primary_key=True)
    code = CharField(max_length=8)
    name = CharField(max_length=120)
    phone = CharField(max_length=12)
    fee = IntegerField()

    class Meta:
        database = db

