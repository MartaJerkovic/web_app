from flask import Blueprint, render_template, url_for

frontend = Blueprint('frontend', __name__, template_folder='templates/frontend')


@frontend.route("/")
def index():
    return render_template ('index.html')