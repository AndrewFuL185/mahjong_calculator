# -*- coding: utf-8 -*-

import multiprocessing
bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count()
pidfile = '/data/var/gunicorn/model.pid' #pid位置
logfile = '/data/logs/gunicorn/model.log' # gunicorn日志，需定义好的位置
