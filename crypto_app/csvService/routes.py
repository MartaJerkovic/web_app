from flask import Flask, Blueprint, request, render_template, url_for, flash, redirect, jsonify, make_response, current_app
import uuid
import jwt
from .models import Transaction
from datetime import datetime, timedelta
from functools import wraps
import csv
from .utils import process_csv


data_processing = Blueprint('data_processing', __name__, template_folder='templates/csvService')



@data_processing.route('/import_csv', methods=['GET', 'POST'])
def import_csv():
    print("Upload route called!")
    if request.method == 'POST':
        process_csv()
    
        return redirect(url_for('reading.home'))
    else:
        print("No file uploaded.")
        return "No file uploaded."