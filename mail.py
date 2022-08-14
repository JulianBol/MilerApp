from flask import (
    Blueprint, render_template
)
from miler.db import get_db 
import mysql.connector

bp = Blueprint('mail', __name__, url_prefix = '/')

@bp.route('/', methods = ['GET'])
def index():
    db, c = get_db()
    c.execute('SELECT * FROM email')
    mails = c.fetchall()
    db.commit()

    return render_template('mails/index.html', mails = mails)