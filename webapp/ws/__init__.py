from flask_socketio import SocketIO
from flask import Blueprint


ws_c = Blueprint('ws_c', __name__, template_folder="templates")

ws = SocketIO()

from webapp.ws import ws_test