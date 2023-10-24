from flask import Flask, Blueprint, render_template, url_for, flash, redirect, jsonify
from userService.routes import token_required
from csvService.models import Transaction

reading = Blueprint('reading', __name__, template_folder='templates/readingService')

@reading.route("/csv")
@token_required
def csv(current_user):
    return render_template ('reading.html')

@reading.route("/home")
@token_required
def home(current_user):
    user_transactions = Transaction.query.filter_by(public_id=current_user.public_id).all()
    return render_template ('reading.html', data=user_transactions)

@reading.route("/watchlist")
@token_required
def watchlist(current_user):
    return render_template ('reading.html')

@reading.route("/profile")
@token_required
def profile(current_user):
    return render_template ('reading.html')