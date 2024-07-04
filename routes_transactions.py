from main import app, jsonify, send_from_directory, render_template, redirect,after_this_request
from controller.TransactionController import *
from controller.CustomersController import *
from controller.ServicesController import *
from controller.OperatorsController import *
import logging
logger = logging.getLogger(__name__)
import sqlite3
import datetime

DB_FILE = 'database_cumo.db'
@app.route('/transactions',  methods=["GET"])
def transactions():
    trxs = TransactionController.list_transactions()
    return render_template('transactions/transaction-list.html', transactions=trxs)



@app.after_request
def add_header(response):
    # Disable caching for all routes
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/transaction_add',  methods=["GET"])
def transaction_add():
    TransactionController.list_transactions
    return render_template('transactions/transaction-add.html')

@app.route('/transaction_add', methods=["POST"])
def transaction_adds():
    ids = request.args.get('id', '0')
    cust_id = request.form['cust_id']
    serv_id = request.form['serv_id']
    cust_nomor = request.form['cust_nomor']
    cust_owner = request.form['cust_owner']
    cust_phone = request.form['cust_phone']
    serv_code = request.form['serv_code']
    serv_name = request.form['serv_name']
    price = request.form['price']
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if ids == '0':
        ids = randint(10000, 99999)
        ts = datetime.datetime.now()
        # Insert new record
        cursor.execute("""
            INSERT INTO Transactions (id, cust_id, serv_id, cust_nomor, cust_owner, cust_phone, serv_code, serv_name, price, created_on)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (ids, cust_id, serv_id, cust_nomor, cust_owner, cust_phone, serv_code, serv_name, price, ts))
    else:
        # Update existing record
        cursor.execute("""
            UPDATE Transactions
            SET cust_id=?, serv_id=?, cust_nomor=?, cust_owner=?, cust_phone=?, serv_code=?, serv_name=?, price=?
            WHERE id=?
            """, (cust_id, serv_id, cust_nomor, cust_owner, cust_phone, serv_code, serv_name, price, ids))

    conn.commit()
    conn.close()

    services = ServicesController.list_services()
    print(services)
    return render_template('transactions/transaction-add.html', services=services)



@app.route("/transaction-delete", methods=["GET"])
def transaction_delete():
    TransactionController.delete_transactions()
    return redirect('/transactions')


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