from model.Services import *
from main import request
from random import randint
import datetime


class ServicesController(object):

    @staticmethod
    def save_services():
        id = request.args.get('id', '0')
        code = request.form['code']
        name = request.form['name']
        many_operator = request.form['many_operators']
        price = request.form['price']
        if id == '0':
            id = randint(10000, 99999)
            ts = datetime.datetime.now().timestamp()
            q = Servs.insert(id=id,  code=str(code), name=str(name),
                        many_operators=many_operator,  price=price, created_on =ts)
            return q.execute()

        query = "update services SET code ={code}, many_operators={ops}, name ='{name}' ," \
                " price ='{price}' WHERE id={id}".format(id=int(id),code=code, ops=many_operator,
                                                         name=name, price=price )
        return db.execute_sql(query)


    @staticmethod
    def detail_services():
        id = request.args.get('id', '0')
        if id == '0':
            Servs.code = ''
            Servs.name = ''
            Servs.price = ''
            Servs.many_operator = ''
            return Servs
        else:
            query = 'select * from services WHERE id={id}' .format(id=int(id))
            cursor = db.execute_sql(query)
            resp = cursor.fetchone()
            Servs.code = resp[1]
            Servs.name = resp[2]
            Servs.price = resp[4]
            Servs.many_operator = resp[3]
            return Servs

    @staticmethod
    def delete_service():
            delete_id = request.args.get('id', '0')
            service = Servs.get(Servs.id == delete_id)
            return service.delete_instance()

    @staticmethod
    def list_services():
        return Servs.select()
