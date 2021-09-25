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
                           operator_name=operator.name,operator_fee=operator.fee,operator_phone=operator.phone
                           )


@app.route("/operator_form", methods=["POST"])
def operator_save():
    error =  False
    error_msg = []
    operator_kode = request.form['code']
    operator_name = request.form['name']

    if operator_kode == "":
        error = True
        error_msg.append("kode belum diisi")

    if operator_name == "":
        error = True
        error_msg.append("nama belum diisi")

    if operator_fee == "":
        error = True
        error_msg.append("harga belum diisi")

    if error:

        return render_template('references/operators/operators-form.html',operator_kode=operator_kode,operator_name=operator_name,
                               error=error,error_msg = error_msg)

    OperatorsController.save_operators()
    return redirect('/success')
    # return render_template('references/customers-form.html' )

@app.route("/operator_delete", methods=["GET"])
def operator_delete():
    OperatorsController.delete_operator()
    return redirect('/operators')

