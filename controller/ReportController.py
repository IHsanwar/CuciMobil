from model.Services import *
from main import request
from random import randint
import datetime, time

class ReportController(object):


    @staticmethod
    def detail_reports():
        id = request.args.get('id', '0')
        if id == '0':
            transaction.code = ''
            transaction.name = ''
            transaction.price = ''
            transaction.many_operator = ''
            return Servs
        else:
            query = 'select * from transaction WHERE id={id}' .format(id=int(id))
            cursor = db.execute_sql(query)
            resp = cursor.fetchone()
            transaction.code = resp[1]
            transaction.name = resp[2]
            transaction.price = resp[4]
            transaction.many_operator = resp[3]
        return Servs