from werkzeug.middleware.proxy_fix import ProxyFix

from .app import app as flask_app


app = ProxyFix(flask_app)
