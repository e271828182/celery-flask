# -*- coding=utf-8 -*-
from . import controller
from webapp.task.tasks import exec_task, exec_task2, kill_celery_task
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


@controller.route('/task2', methods=['GET', 'POST'])
def task2():
    a = request.args.get("a", default=12)
    b = request.args.get("b", default=12)
    name = request.args.get("name", default="aaa")
    exec_task2.apply_async(args=(a, b), task_id=name)
    return "task"


@controller.route('/kill_task', methods=['GET', 'POST'])
def kill_task():
    name = request.args.get("name", default="aaa")
    kill_celery_task.apply_async(args=(name, ), priority=0)
    return "task"
