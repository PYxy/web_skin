from __future__ import absolute_import, unicode_literals

from celery import shared_task
import datetime
from .app_public import user_handle_sync_function
from pkg.decorator.base_decorator import check_sync, async_handle
from logger_settings.logger import console
from web_skin.celery_server import app

@shared_task
@async_handle(console, "user_sync")  # 异步信息响应
@check_sync(console, "user_sync")  # 参数按需添加
def user_handle_sync_(*args, **kwargs):
    message_dict = user_handle_sync_function(**kwargs)
    return message_dict


@app.task(ignore_result=True)
def task_training_in_rotation():
    print(f"定时任务: {datetime.datetime.now()}")