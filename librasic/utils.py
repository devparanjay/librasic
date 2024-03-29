from flask import request, make_response, current_app
from functools import wraps


def check_auth(f):
    @wraps(f)
    def deco_auth(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == current_app.config["LIBRARIAN_USERNAME"] and auth.password == current_app.config["LIBRARIAN_PASSWORD"]:
            return f(*args, **kwargs)
        return make_response("<h1>Access was denied.</h1><br><h2>Contact administrator for credentials.</h2>", 401, {'WWW-Authenticate': 'Basic realm="Login to Librasic"'})

    return deco_auth

def check_fees(f):
    @wraps(f)
    def deco_feecheck(*args, **kwargs):
        pass
    return deco_feecheck