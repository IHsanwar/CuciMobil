from main import app, jsonify, send_from_directory, render_template, redirect
from controller.OperatorsController import *

@app.route("/operators", methods=["GET"])
def operators():
    operators = OperatorsController.list_operators()
    return render_template('references/operators/operators-list.html', operators=operators)

@app.route("/operator_form", methods=["GET"])
def operator_form():
    operator = OperatorsController.detail_operators()

    return render_template('references/operators/operators-form.html',operator_kode=operator.code,
                           operator_name=operator.name,operator_fee=operator.fee,operator_phone=operator.phone)


@app.route("/operator_form", methods=["POST"])
def operator_save():
    print("8)")
    OperatorsController.save_operators()
    return redirect('/success')
    # return render_template('references/customers-form.html' )

@app.route("/operator_delete", methods=["GET"])
def operator_delete():
    OperatorsController.delete_operator()
    return redirect('/operators')

