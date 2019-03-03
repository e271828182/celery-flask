from flask import Blueprint


controller = Blueprint('controller', __name__)


from webapp.controller import test1