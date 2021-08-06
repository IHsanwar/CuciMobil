from main import app, jsonify, send_from_directory, render_template, redirect
from controller.CustomersController import *


# Customers
@app.route("/customers", methods=["GET"])
def customers():
    customers = CustomerController.list_customers()
    return render_template('references/customers/customers-list.html', customers=customers )


@app.route("/customer_form", methods=["GET"])
def customer_form():
    customer = CustomerController.detail_customers()
    return render_template('references/customers/customers-form.html', customer_nopol=customer.nopol,
                           customer_owner=customer.owner, customer_phone=customer.phone )


@app.route("/customer_form", methods=["POST"])
def customer_save():
    CustomerController.save_customers()
    return redirect('/success')
    # return render_template('references/customers-form.html' )

@app.route("/customer_delete", methods=["GET"])
def customer_delete():
    CustomerController.delete_customer()
    return redirect('/customers')

