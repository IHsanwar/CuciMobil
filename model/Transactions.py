from .connect import *


class Transactions(Model):
    id = IntegerField()
    cust_id = IntegerField()
    serv_id = IntegerField()
    cust_nomor = CharField()
    cust_owner = CharField()
    cust_phone = CharField()
    serv_code = CharField()
    serv_name = CharField()
    price = IntegerField()
    created_on = IntegerField()

    class Meta:
        database = db