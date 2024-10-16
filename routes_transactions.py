from main import app, jsonify, send_from_directory, render_template, redirect,after_this_request,url_for
from controller.TransactionController import *
from controller.CustomersController import *
from controller.ServicesController import *
from controller.OperatorsController import *
from controller.CustomersController import *
from datetime import date
import peewee

import logging
logger = logging.getLogger(__name__)
import sqlite3
import datetime

DB_FILE = 'database_cumo.db'
@app.route('/transactions',  methods=["GET"])
def transactions():
    trxs = TransactionController.list_transactions()
    return render_template('transactions/transaction-list.html', transactions=trxs)

@app.route('/transaction_add', methods=['GET', 'POST'])
def transaction_form():
    if request.method == 'POST':
        name = request.form['name']
        service_id = request.form['serv_id']
        cus_id = request.form['cus_id']
        dates = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            service = Servs.get_by_id(service_id)
            customer = Customers.get_by_id(cus_id)
            transaction = Transactions.create(
                cust_owner=name,
                cust_id=customer.id,
                cust_nomor=customer.nopol,
                cust_phone=customer.phone,
                serv_id=service,
                price=service.price,
                serv_name=service.name,
                serv_code=service.code,
                created_on=dates
            )
            # Redirect to bill page
            return redirect(url_for('bill', transaction_id=transaction.id))
        
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            message = 'Error creating transaction!'
            return render_template('transactions/transaction-add.html', services=Servs.select(), nopol=Customers.select(), error=message)

    else:
        return render_template('transactions/transaction-add.html', services=Servs.select(), customer=Customers.select())

@app.route("/transaction-delete", methods=["GET"])
def transaction_delete():
    TransactionController.delete_transactions()
    return redirect('/transactions')


@app.route('/transaction-bill/<int:transaction_id>')
def bill(transaction_id):
    transaction = Transactions.get_by_id(transaction_id)
    return render_template('transactions/bill.html', transaction=transaction)

@app.route('/list_nopol',  methods=["GET"])
def nopols():
    nopols = CustomerController.list_nopol()
    datas = []
    for np in nopols:
        d = {}
        d['name'] = np.nopol
        d['id'] = np.id
        datas.append(d)

    return jsonify(datas), 200