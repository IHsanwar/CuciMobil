from model.Operators import *
from main import request
from random import randint

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
        if id == '0':
            id = randint(100000, 999999)
            row = {
                'id': id,
                'name': name,
                'phone': phone,
                'code': code,
                'fee': fee
            }
            return Operators.insert(row).execute()

        else:
            row = {
                'name': name,
                'phone': phone,
                'code': code,
                'fee': fee
            }
            return Operators.update(row).where(Operators.id == int(id)).execute()

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