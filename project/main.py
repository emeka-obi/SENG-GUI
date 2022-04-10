from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from utils.logging import Log
from .models import Coursedata


main = Blueprint('main', __name__)

@main.route('/')
def cover_page():
    #  Logs success if the route executes as normal
    Log.log.info("200: Template returned successfully")
    return render_template('cover.html')

@main.route('/coursedata')
@login_required
def coursedata():
    try:
        coursedata = Coursedata.query.all()      
        Log.log.info(' 200: Data Queried successfully')
        return render_template('tables.html', coursedata=coursedata, name=current_user.name)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        Log.log.warn("500: Unexpected error occurred")
        return hed + error_text