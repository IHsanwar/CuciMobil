from main import app, jsonify, send_from_directory, render_template, redirect
from controller.ServicesController import *


@app.route("/services", methods=["GET"])
def services():
    services = ServicesController.list_services()
    return render_template('references/services/services-list.html', services=services)


@app.route("/service_form", methods=["GET"])
def service_form():
    service = ServicesController.detail_services()
    print(service)
    return render_template('references/services/services-form.html',services_name=service.name,
                           services_code=service.code,services_price=service.price)

@app.route("/service_form", methods=["POST"])
def service_save():
    print("8)")
    ServicesController.save_services()
    return redirect('/success')
    # return render_template('references/customers-form.html' )

@app.route("/service_delete", methods=["GET"])
def service_delete():
    ServicesController.delete_service()
    return redirect('/services')