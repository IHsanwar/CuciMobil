from model.Services import *
from main import request
from random import randint
import datetime


class ServicesController(object):
    @staticmethod
    def list_services():
        return Services.select()

    @staticmethod
    def save_services():


        id = request.args.get('id', '0')
        code = request.form['code']
        name = request.form['name']
        many_operator = request.form['many_operators']
        price = request.form['price']
        print(id)
        if id == '0':
            id = randint(10000, 99999)
            ts = datetime.datetime.now().timestamp()
            return Services.create(id=id,
                                    code=code,
                                    many_operator=many_operator,
                                    name=name,
                                    price=price
                                    )


        return operators.save()

    @staticmethod
    def detail_services():
        id = request.args.get('id', '0')
        print(id)
        if id == '0':
            Services.code = ''
            Services.name = ''
            Services.price = ''
            Services.many_operator = ''
            return Services
        else:
            print(id)
            print(Services)
            x= Services.get(Services.id == int(id))
            print(x)
            return x

    @staticmethod
    def delete_service():
            delete_id = request.args.get('id', '0')
            service = Services.get(Services.id == delete_id)
            return service.delete_instance()


