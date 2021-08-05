from model.Customers import *
from main import request
from random import randint
import datetime


class CustomerController(object):

    @staticmethod
    def detail_customers( ):
        id = request.args.get('id', '0')
        if id == '0':
            Customers.nopol = ''
            Customers.owner = ''
            Customers.phone = ''
            Customers.vehicle_model = 1
            return Customers

        return Customers.get(Customers.id == int(id))

    @staticmethod
    def list_customers():
        customers = Customers.select()
        datas = []
        for cust in customers:
            if cust.vehicle_model == 1:
                cust.vehicle_model = 'Mobil'
            else:
                cust.vehicle_model = 'Sepeda motor'
            datas.append(cust)

        return datas

    @staticmethod
    def save_customers( ):
        id = request.args.get('id', '0')
        nopol = request.form['nopol']
        owner = request.form['owner']
        phone = request.form['phone']
        vehicle_model = request.form['vehicle_model']

        if id == '0':
            id = randint(10000, 99999)
            ts = datetime.datetime.now().timestamp()
            return Customers.create(id=id,
                                    nopol=nopol,
                                    phone=phone,
                                    owner=owner,
                                    vehicle_model=vehicle_model,
                                    created_on=ts)
        else:
            customers = Customers.get(Customers.id == int(id))
            customers.owner = owner
            customers.phone = phone
            customers.nopol = nopol
            customers.vehicle_model = vehicle_model
            return customers.save()


    @staticmethod
    def list_nopol():
        q = request.args.get('q', '')
        customers = Customers.select()
        return customers