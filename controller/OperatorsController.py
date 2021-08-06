from model.Operators import *
from main import request
from random import randint
import datetime

class OperatorsController(object):


    @staticmethod
    def list_operators():
        operators = Operators.select()
        datas = []
        return Operators.select()


    @staticmethod
    def save_operators():


        id = request.args.get('id', '0')
        code = request.form['code']
        name = request.form['name']
        phone = request.form['phone']
        fee = request.form['fee']
        print(id)
        if id == '0':
            id = randint(10000, 99999)
            ts = datetime.datetime.now().timestamp()
            return Operators.create(id=id,
                                    code=code,
                                    phone=phone,
                                    name=name,
                                    fee=fee
                                    )

        else:
            operators = Operators.get(Operators.id == int(id))
            operators.name = name
            operators.phone = phone
            operators.code = code
            operators.fee = fee
            return operators.save()

    @staticmethod
    def detail_operators():
        id = request.args.get('id', '0')
        if id == '0':
            Operators.code = ''
            Operators.name = ''
            Operators.phone = ''
            Operators.fee = ''
            return Operators

        return Operators.get(Operators.id == int(id))

    @staticmethod
    def delete_operator():
        delete_id = request.args.get('id', '0')
        operator = Operators.get(Operators.id == delete_id)
        return operator.delete_instance()