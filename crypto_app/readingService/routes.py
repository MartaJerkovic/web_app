from flask import Flask, Blueprint, render_template, url_for, flash, redirect, jsonify


reading = Blueprint('reading', __name__, template_folder='templates/readingService')

@reading.route("/records/<public_id>")
def records(public_id):
    return render_template ('reading.html')