from flask import Blueprint


user_bp = Blueprint('user', __name__, subdomain='cms')

@user_bp.route('/profile/')
def profile():
    return "这是用户界面"


@user_bp.route('/setting/')
def setting():
    return "这是用户设置界面"
