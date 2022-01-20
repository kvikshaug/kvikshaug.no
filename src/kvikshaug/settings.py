import os


class Configuration:
    ENVIRONMENT = os.environ["ENVIRONMENT"]
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s [%(levelname)s] [%(name)s] "
                "%(filename)s:%(funcName)s:%(lineno)d | %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            }
        },
        "loggers": {
            # Add any noisy loggers here with a higher loglevel.
            "parso": {"level": "INFO", "handlers": ["console"]}
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }


if os.environ["ENVIRONMENT"] not in ("production", "testing", "development"):
    raise ValueError(f"Unknown environment: {os.environ['ENVIRONMENT']}")

if os.environ["ENVIRONMENT"] == "production":
    Configuration.DEBUG = False
    Configuration.SECRET_KEY = bytes.fromhex(os.environ["SECRET_KEY"])
    Configuration.LOGGING["root"]["level"] = "INFO"

if os.environ["ENVIRONMENT"] == "testing":
    Configuration.DEBUG = True
    Configuration.SECRET_KEY = os.urandom(64)
    Configuration.TESTING = True

if os.environ["ENVIRONMENT"] == "development":
    Configuration.DEBUG = True
    Configuration.SECRET_KEY = b"development"
