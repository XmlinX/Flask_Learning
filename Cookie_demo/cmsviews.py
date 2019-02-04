from flask import Blueprint, request


bp = Blueprint('cms', __name__, subdomain='cms')


@bp.route('/')
def Index():
    username = request.cookies.get('username')
    return username or "没有获取到cookie"