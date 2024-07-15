from flask import Flask, jsonify, send_from_directory, render_template, request, redirect ,flash,after_this_request
# from pyfladesk import init_gui
import time

app = Flask(__name__, template_folder="./templates")

from routes import *
from routes_customers import *
from routes_operators import *
from routes_transactions import *
from routes_services import *
from routes_report import *
if __name__ == '__main__':
    # init_gui(app, port=5000, width=1100, height=600,  window_title="Aplikasi cuci mobil", argv=None)
    app.run(port=7500)