from main import app, jsonify, send_from_directory, render_template, redirect
from controller.TransactionController import *
from controller.CustomersController import *
from controller.ServicesController import *


@app.route('/transactions',  methods=["GET"])
def transactions():
    trxs = TransactionController.list_transactions()
    return render_template('transactions/transaction-list.html', transactions=trxs)


@app.route('/transaction_add',  methods=["GET"])
def transaction_add():
    datas = TransactionController.prepare_data_customer()
    services = ServicesController.list_services()
    return render_template('transactions/transaction-add.html' , services= services )


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