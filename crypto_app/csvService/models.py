from flask import Flask
from userService.extensions import db


class Transaction(db.Model):
    __bind_key__ = 'transactions'
    __tablename__ = "Transactions"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    transaction_type = db.Column(db.String, nullable=True)
    asset = db.Column(db.String, nullable=False)
    quantity_transacted = db.Column(db.String, nullable=False)
    spot_price_currency = db.Column(db.String, nullable=False)
    spot_price_at_transaction = db.Column(db.String, nullable=False)
    subtotal_without_fees = db.Column(db.String, nullable=False)

