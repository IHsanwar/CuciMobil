from main import app, jsonify, send_from_directory, render_template, redirect
from controller.ReportController import *
from flask import make_response
import pdfkit

@app.route('/monthly_report', methods=["GET"])
def monthly_report():
    month = request.args.get('month', default=datetime.now().strftime("%Y-%m"))
    transactions = ReportController.get_monthly_report(month)
    
    return render_template('report/data_laporan_bulanan.html', transactions=transactions, month=month)

@app.route('/download_monthly_report', methods=["GET"])
def download_monthly_report():
    month = request.args.get('month', default=datetime.now().strftime("%Y-%m"))
    transactions = ReportController.get_monthly_report(month)
    
    html = render_template('report/laporan_bulanan.html', transactions=transactions, month=month)
    
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    pdf = pdfkit.from_string(html, False, configuration=config)
    
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=monthly_report_{month}.pdf'
    
    return response

@app.route('/report_operator' ,methods=["GET"])
def operator_report():
    transaction_operators = ReportController.get_operator_report()
    
    return render_template('report/laporan_operator.html', transaction_operators=transaction_operators)