from flask import Blueprint, render_template

bp = Blueprint('views', __name__, url_prefix='/projects')

@bp.route('crm-freelancers')
def crm():
    return render_template("crm-freelancers.html")

@bp.route('task-api')
def api():
    return render_template("task-api.html")

@bp.route('website')
def website():
    return render_template("agency-website.html")




