from model.Customers import *
from main import request
from random import randint
import datetime
import qrcode
from io import BytesIO
from PIL import Image
import base64
import datetime
from random import randint
from flask import request

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
            
            # Convert the QR code into base64 image format
            qr_code_image = f"data:image/png;base64,{cust.qr_code}"
            cust.qr_code_image = qr_code_image  # Add the image string to the customer object
            
            datas.append(cust)
        
        return datas

    @staticmethod
    def save_customers():
        id = request.args.get('id', '0')
        nopol = request.form['nopol']
        owner = request.form['owner']
        phone = request.form['phone']
        vehicle_model = request.form['vehicle_model']

        if id == '0':
            id = randint(10000, 99999)
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            id = randint(100000, 999999)

            # Generate QR Code for the id
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(id))
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

            buffered = BytesIO()
            img.save(buffered, format="PNG")
            qr_code_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

            row = {
                'id': id,
                'nopol': nopol,
                'phone': phone,
                'owner': owner,
                'created_on': ts,
                'vehicle_model': vehicle_model,
                'qr_code': qr_code_base64  # Assuming you save the QR code in base64 in DB
            }

            return Customers.insert(row).execute()

        else:
            row = {
                'owner': owner,
                'phone': phone,
                'nopol': nopol,
                'vehicle_model': vehicle_model
            }
            return Customers.update(row).where(Customers.id == int(id)).execute()


    @staticmethod
    def delete_customer():
        delete_id = request.args.get('id', '0')
        customer = Customers.get(Customers.id == delete_id)
        return customer.delete_instance()


    # Untuk cari data nomor polisi
    @staticmethod
    def list_nopol():
        q = request.args.get('q', '')
        customers = Customers.select()
        return customers