from flask import Flask, Blueprint, render_template, url_for, flash, redirect, jsonify


reading = Blueprint('reading', __name__, template_folder='templates/readingService')

@reading.route("/home/<public_id>")
def home(public_id):
    return render_template ('reading.html', public_id = public_id)

@reading.route("/watchlist/<public_id>")
def watchlist(public_id):
    return render_template ('reading.html', public_id = public_id)

@reading.route("/profile/<public_id>")
def profile(public_id):
    return render_template ('reading.html', public_id = public_id)