from flask import (
    Blueprint, current_app, redirect
)

bp = Blueprint('index', __name__,)


@bp.route('/')
def index():
    return redirect(current_app.config['WEB'], code=302)
