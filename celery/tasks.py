#windows cmd：celery -A tasks worker --loglevel=info --pool=solo
#https://juejin.im/entry/586c918cac502e12d632ac09


# from celery import Celery

# brokers = 'redis://10.242.130.157:6379/8'
# backend = 'redis://10.242.130.157:6379/9'

# app = Celery('main',broker=brokers,backend=backend)

# @app.task
# def add(x,y):
#     return x+y

