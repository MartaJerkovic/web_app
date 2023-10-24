from flask import Flask, request, current_app, redirect, flash
from .models import Transaction
from userService.extensions import db
from werkzeug.utils import secure_filename
import csv
import jwt
import datetime
import pandas as pd


ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_csv():
    if 'csv-file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    csv_file = request.files['csv-file']
    if csv_file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if csv_file and allowed_file(csv_file.filename):
        filename = secure_filename(csv_file.filename)

        print(f"File Name: {csv_file.filename}")
        print(f"Content Type: {csv_file.content_type}")

        try:
            token = request.cookies.get('token')
            decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            public_id = decoded_token['public_id']
            print(public_id)

            #csv_data = TextIOWrapper(csv_file, encoding='utf-8')

            #csv_reader = csv.DictReader(csv_data)

            df = pd.read_csv(csv_file, delimiter=',', skiprows=7)
            df.fillna(0, inplace=True)
            print(df)

            for index, row in df.iterrows():
        
                timestamp_string = row.get('Timestamp', '')
                timestamp = datetime.datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%SZ')

                transaction_type = row.get('Transaction Type', '')
                asset = row.get('Asset', '')
                quantity_transacted = row.get('Quantity Transacted', '')
                spot_price_currency = row.get('Spot Price Currency', '')
                spot_price_at_transaction = row.get('Spot Price at Transaction', '')
                subtotal_without_fees = row.get('Subtotal', '')

                transaction = Transaction(
                    public_id=public_id,
                    timestamp=timestamp,
                    transaction_type=transaction_type,
                    asset=asset,
                    quantity_transacted=quantity_transacted,
                    spot_price_currency=spot_price_currency,
                    spot_price_at_transaction=spot_price_at_transaction,
                    subtotal_without_fees=subtotal_without_fees,
                )

                db.session.add(transaction)

            db.session.commit()
            flash(f'Success! Your CSV file has been imported!', 'success')
        
        except Exception as e:
            db.session.rollback()
            print(f"Error: {str(e)}")
            flash(f'Error processing the CSV file: {str(e)}', 'error')
            return redirect(request.url)