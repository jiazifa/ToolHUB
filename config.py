import os
from typing import List

REDIS_URI = os.environ.get("REDIS_URI", "redis://redis:6379/")
"""Celery 配置"""

CELERY_RESULT_BACKEND = REDIS_URI

BROKER_URL = REDIS_URI + "0"

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_TASK_SERIALIZER = "json"

CELERY_RESULT_SERIALIZER = "json"

CELERY_ACCEPT_CONTENT = ["json"]

from datetime import timedelta  # noqa
from kombu import Exchange, Queue  # noqa
# 导入Task所在的模块，所有使用celery.task装饰器装饰过的函数，所需要把所在的模块导入
# 我们之前创建的几个测试用函数，都在handlers.async_tasks和handlers.schedules中
# 所以在这里需要导入这两个模块，以str表示模块的位置，模块组成tuple后赋值给CELERY_IMPORTS
# 这样Celery在启动时，会自动找到这些模块，并导入模块内的task
CELERY_IMPORTS = ('celery_tasks.tasks')

# 是否忽略结果
CELERY_IGNORE_RESULT = False

# 定义定时任务
CELERYBEAT_SCHEDULE = {
    'caihongpi.fetch': {
        'task': 'celery_tasks.one_word.caihongpi',
        'schedule': timedelta(seconds=60),
        'args': ()
    },
    'acib.fetch': {
        'task': 'celery_tasks.one_word.acib',
        'schedule': timedelta(seconds=60 * 60 * 24),
        'args': ()
    },
    'hitokoto.fetch': {
        'task': 'celery_tasks.one_word.hitokoto',
        'schedule': timedelta(seconds=60),
        'args': ()
    },
    'lovelive.fetch': {
        'task': 'celery_tasks.one_word.lovelive',
        'schedule': timedelta(seconds=60),
        'args': ()
    },
    'wufazhuce.fetch': {
        'task': 'celery_tasks.one_word.wufazhuce',
        'schedule': timedelta(seconds=60 * 60 * 24),
        'args': ()
    }
}


RSS_SOUECES: List[str] = [
    "https://www.zhihu.com/rss",
]

try:
    from locale_settings import *  # noqa
except ImportError:
    pass
