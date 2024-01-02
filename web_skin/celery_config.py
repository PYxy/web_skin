
from celery import platforms
from celery.schedules import crontab

# 开启worker
# celery -A web_skin worker -l info -P eventlet
# 监控定时任务
# celery -A web_skin beat -l info -S django

platforms.C_FORCE_ROOT = True


class CeleryConfig(object):
    BROKER_URL = 'redis://xx.xx.xx.xx:6379/5'
    CELERY_RESULT_BACKEND = 'redis://xx.xx.xx.xx:6379/6'
    CELERY_TASK_SERIALIZER = 'json'  # " json从4.0版本开始默认json,早期默认为pickle（可以传二进制对象）
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json', 'pickle']
    CELERY_ENABLE_UTC = False  # 启用UTC时区
    CELERY_TIMEZONE = 'Asia/Shanghai'  # 上海时区
    CELERYD_HIJACK_ROOT_LOGGER = False  # 拦截根日志配置
    CELERYD_MAX_TASKS_PER_CHILD = 1  # 每个进程最多执行1个任务后释放进程（再有任务，新建进程执行，解决内存泄漏）
    # 设置worker数
    CELERYD_CONCURRENCY = 3

    # 定时任务
    CELERYBEAT_SCHEDULE = {
        'do-every-60-seconds': {
           'task': 'app01.tasks.task_training_in_rotation',  # 任务名
           'schedule': crontab(minute="*"),  # 每60s执行一次该任务
        },
    }
