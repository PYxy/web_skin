from logger_settings.logger import console


def user_create(**kwargs):
    console.info("user_create 的真正处理")
    return {"data": "user_create 同步处理成功", "code": 200}


def user_handle_sync_function(**kwargs):
    console.info(f"user_create_sync 异步的真正处理:{kwargs}")
    return kwargs
