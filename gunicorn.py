import os

import gevent.monkey


# Ensure gevent is monkeypatched before ssl is imported (gunicorn does this too
# late). This is only necessary when `preload_app` is True. The gevent warning
# is still printed, but testing shows that recursion errors do not occur (eg. on
# use of `requests`) when monkey-patching here.
# See also https://github.com/gevent/gevent/issues/1016 and
# https://github.com/benoitc/gunicorn/issues/1566
gevent.monkey.patch_all()


_config = os.environ["ENVIRONMENT"]

bind = "0.0.0.0:8000"
worker_class = "gevent"
workers = 1
timeout = 30

if _config == "production":
    preload_app = True
    accesslog = "logs/access.log"
    access_log_format = '''%(t)s %({x-forwarded-for}i)s %(u)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s'''
else:
    reload = True
    accesslog = "-"
    access_log_format = '''%(t)s "%(r)s" %(s)s %(b)s %(L)s'''
