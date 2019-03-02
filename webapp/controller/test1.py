from . import controller
from webapp.task.tasks import exec_task


@controller.route('/hello', methods=['GET', 'POST'])
def hello():
    return "hello"


@controller.route('/task', methods=['GET', 'POST'])
def task():
    exec_task.delay(23, 42)
    return "task"