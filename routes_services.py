from main import app, jsonify, send_from_directory, render_template, redirect
from controller.ServicesController import *


@app.route("/services", methods=["GET"])
def services():
    services = ServicesController.list_services()
    print(services)
    return render_template('references/services/services-list.html', services=services)


@app.route("/service_form", methods=["GET"])
def service_form():
    serv = ServicesController.detail_services()
    return render_template('references/services/services-form.html',service_name=serv.name,
                           service_code=serv.code,service_price=serv.price,service_many_operators=serv.many_operator)

@app.route("/service_form", methods=["POST"])
def service_save():
    ServicesController.save_services()
    return redirect('/success')
    # return render_template('references/customers-form.html' )

@app.route("/service_delete", methods=["GET"])
def service_delete():
    ServicesController.delete_service()
    return redirect('/services')