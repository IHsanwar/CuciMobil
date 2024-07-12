from model.Transactions import *
from model.Services import *
from main import request
from random import *
from datetime import datetime

class TransactionController(object):

    @staticmethod
    def list_transactions():
        return Transactions.select()

    @staticmethod
    def prepare_data_customer():
        response = {'services': Servs.select()}

        return response
    
    @staticmethod
    def save_transaction():
        ids = request.args.get('id', '0')
        cust_id = request.form['cust_id']
        serv_id = request.form['serv_id']
        cust_nomor = request.form['cust_nomor']
        cust_owner = request.form['cust_owner']
        cust_phone = request.form['cust_phone']
        serv_code = request.form['serv_code']
        serv_name = request.form['serv_name']
        price = request.form['price']

        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()

            if ids == '0':
                ids = randint(10000, 99999)
                ts =randint(10000, 99999)
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
        except Exception as e:
            return f'Failed to save transaction: {str(e)}'
        
    @staticmethod
    def delete_transactions():
        delete_id = request.args.get('id', '0')
        deltra = Transactions.get(Transactions.id == delete_id)
        return deltra.delete_instance()
    

    @staticmethod
    def detail_transactions():
        id = request.args.get('id', '0')
        if id == '0':
            Transactions.cust_id = ''
            Transactions.serv_id = ''
            Transactions.cust_nomor = ''
            Transactions.cust_owner = ''
            Transactions.cust_phone = ''
            Transactions.serv_code =''
            Transactions.price = ''
            return Transactions

        return Transactions.get(Transactions.id == int(id))