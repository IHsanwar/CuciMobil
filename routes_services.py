from main import app, jsonify, send_from_directory, render_template, redirect
from controller.ServicesController import *


@app.route("/services", methods=["GET"])
def services():
    services = ServicesController.list_services()
    print(services)
    return render_template('references/services/services-list.html', services=services)


@app.route("/service_form", methods=["GET"])
def service_form():
    serv =  ServicesController.detail_services()
    return render_template('references/services/services-form.html',service_name=serv.name,
                           service_code=serv.code,service_price=serv.price,service_many_operators=serv.many_operator)

@app.route("/service_form", methods=["POST"])
def service_save():

    error = False
    error_msg = []
    service_kode = request.form['code']
    service_name = request.form['name']
    service_fee = request.form['price']
    service_many = request.form['many_operators']

    if service_kode == "":
        error = True
        error_msg.append("kode belum diisi")


    if service_name == "":
        error = True
        error_msg.append("nama belum diisi")

    if service_fee == "":
        error = True
        error_msg.append("harga belum diisi")

    if service_many == "":
        error= True
        error_msg.append("operator belum  diisi")
    if error:
        return render_template('references/services/services-form.html', service_kode=service_kode,
                               service_name=service_name,
                               error=error, error_msg=error_msg)
    
    ServicesController.save_services()
    return redirect('/success')

    # return render_template('references/customers-form.html' )

@app.route("/service_delete", methods=["GET"])
def service_delete():
    ServicesController.delete_service()
    return redirect('/services')

@app.route('/service_details/<int:serv_id>', methods=["GET"])
def service_detail(serv_id):
    try:
        service = Servs.get(Servs.serv_id == serv_id)
        return jsonify({"serv_id": service.serv_id, "price": service.price, "serv_code": service.serv_code})
    except Servs.DoesNotExist:
        return jsonify({"error": "Service not found"}), 404
