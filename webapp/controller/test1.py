from . import controller
from webapp.task.tasks import exec_task
from flask import request


@controller.route('/hello', methods=['GET', 'POST'])
def hello():
    return "hello"


@controller.route('/task', methods=['GET', 'POST'])
def task():
    a = request.args.get("a", default=12)
    b = request.args.get("b", default=12)
    exec_task.delay(int(a), int(b))
    return "task"
