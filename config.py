import os

REDIS_URI = os.environ.get("REDIS_URI", "redis://0.0.0.0:6379/")
"""Celery 配置"""

CELERY_RESULT_BACKEND = REDIS_URI

BROKER_URL = REDIS_URI + "0"

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_TASK_SERIALIZER = "json"

CELERY_RESULT_SERIALIZER = "json"

CELERY_ACCEPT_CONTENT = ["json"]

try:
    from locale_settings import *
except ImportError:
    pass
