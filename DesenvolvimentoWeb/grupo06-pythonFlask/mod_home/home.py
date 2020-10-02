from flask import Blueprint, render_template

bp_home = Blueprint('home', __name__, template_folder='templates')

@bp_home.route("/", methods=['GET'])
def formHome():
    return render_template("formHome.html")