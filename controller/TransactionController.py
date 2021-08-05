from model.Transactions import *
from model.Services import *
from main import request


class TransactionController(object):

    @staticmethod
    def list_transactions():
        return Transactions.select()

    @staticmethod
    def prepare_data_customer():
        response = {'services': Services.select()}

        return response
