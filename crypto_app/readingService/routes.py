from flask import Flask, Blueprint, render_template, url_for, flash, redirect, jsonify


reading = Blueprint('reading', __name__, template_folder='templates/readingService')

@reading.route("/records")
def records():
    return render_template ('reading.html')