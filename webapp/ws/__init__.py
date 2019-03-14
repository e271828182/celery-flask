from flask_socketio import SocketIO
from flask import Blueprint


ws = Blueprint('ws_c', __name__, template_folder="templates")

socketio = SocketIO()

from webapp.ws import ws_test