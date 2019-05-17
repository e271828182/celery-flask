# -*- coding=utf-8 -*-
import datetime
from time import sleep

from . import celery


@celery.task()
def exec_task(a):
    print(a)
    with open("/home/star/celery_test/log.txt", 'a') as f:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))