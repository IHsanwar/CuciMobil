from model.Services import *
from main import request
from random import randint
import sqlite3
from datetime import datetime

class ReportController:
    
    @staticmethod
    def get_monthly_report(month):
        conn = sqlite3.connect('./database_cumo.db')
        cursor = conn.cursor()
        
        # Define the start and end dates for the month
        start_date = datetime.strptime(month, "%Y-%m").replace(day=1)
        end_date = (start_date.replace(month=start_date.month + 1) if start_date.month < 12 
                    else start_date.replace(year=start_date.year + 1, month=1))
        
        # Query to get transactions within the month
        query = """
        SELECT * FROM transactions
        WHERE created_on >= ? AND created_on < ?
        """
        cursor.execute(query, (start_date, end_date))
        repo = cursor.fetchall()
        
        conn.close()
        return repo
