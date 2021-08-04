from flask import Flask, jsonify, send_from_directory, render_template, request, redirect
from pyfladesk import init_gui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import time

app = Flask(__name__, template_folder="./templates")

from routes import *

if __name__ == '__main__':
    init_gui(app, port=5000, width=1100, height=600,
             window_title="Aplikasi cuci mobil", argv=None)
    # app.run(port=5000)