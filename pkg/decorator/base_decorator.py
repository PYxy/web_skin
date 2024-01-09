from functools import wraps
from pkg.support_function import param_change, async_to_php


# check_out_param_fbv 参数检测装饰器
def check_out_param(check_class, parma_dict, logger):
    """
    用于检查请求参数的合法性
    :param logger:        日志对象
    :param check_class:  检查类
    :param parma_dict:   检查dict (每个app 中的 param_dict 中的param )
    :return:
    """

    def decorator(func):
        @wraps(func)
        def pick(*args, **kwargs):
            request = args[1]
            try:
                # print(args)
                title = args[0].__class__.__name__
                logger.debug(f"{'=' * 20}{title}.{request.method}{'=' * 20}")
                method_type = param_change(request)
                assert isinstance(method_type, dict), method_type
                # logger.debug(f'请求全路径-{request.path[1:]}')
                logger.debug(f'请求路径:{request.path[1:]}')
                # 实例定义的时候自动进行 参数校验
                check_instance = check_class(f"{request.path[1:].split('/')[-1]}_{request.method.lower()}", parma_dict,
                                             method_type, logger)
                # 获取check_instance 的校验结果
                assert check_instance.key, check_instance.err
                logger.info(f"参数校验通过,继续传递的参数:{check_instance.param_return}")
                return func(*args, **check_instance.param_return)
            except Exception as e:
                key, err = 0, str(e)
                logger.error(f'line(check_out_param)>>{str(e.__traceback__.tb_lineno)}  =>{str(e)}')
                # 异常直接终止 返回给前端
                return {"code": key, "errmsg": err}
            # finally:
            #     # 这里就是不管异常情况 只把检查结果 透传到被装饰器的函数中
            #     logger.debug(data.param_return)
            #     return func(*args, **data.param_return)

        return pick

    return decorator


# check_sync 可以认为是针对不同的操作类型 判断当前情况是否运行执行之类的二次检测
def check_sync(logger, title):
    """
    异步任务前的检测
    :param title:  操作类型
    :param logger:
    :return:
    """

    # 内部定义函数 建议定义在外面
    def support_user_creat(**kwargs):
        # 根据不同的异步任务做不同的操作(后续可以把中间检测、过渡的参数或者状态传递下去)
        kwargs["new_param"] = "在检查函数中新增加的参数"
        # 方法中可以直接抛出异常
        # assert 0,"异常信息"
        return kwargs

    sync_dict = {"user_sync": support_user_creat}

    def decorator(func):

        @wraps(func)
        def pick(**kwargs):
            # 整个检测后的状态
            code, errmsg = 1, ""
            try:
                kwargs = sync_dict[title](**kwargs)
            except Exception as e:
                errmsg = str(e)
                logger.error(f'line(check_sync)>> {str(e.__traceback__.tb_lineno)} =>{errmsg}')
                code, kwargs['errmsg'] = 0, errmsg

            finally:
                if not code:
                    # 有异常就直接响应
                    return {"code": code, "errmsg": errmsg}
                else:
                    # 打印检测后 最新的参数,再交给下一个函数继续执行
                    logger.debug(kwargs)
                    return func(**kwargs)

        return pick

    return decorator


def async_handle(logger, title):
    """
    异步任务结果响应装饰器
    :param logger:  日志对象
    :param title:   异步任务名称 可以根据名称做一些个性化操作
    :return:
    """

    def decorator(func):
        @wraps(func)
        def pick(**kwargs):

            message_dict = {}
            try:
                # 获取上一个装饰器返回的处理结果
                logger.debug(f"前面的装饰器处理好的所有的参数:{kwargs}")
                # 根据处理结果的内容来判断是否可以进行 珍真正的函数操作
                # 异步任务建议都带一个 task_id
                task_id = kwargs.get('task_id')

                # 输出任务结果 异步响应给接收方
                message_dict = func(**kwargs)
            except Exception as e:
                logger.error('line>>' + str(e.__traceback__.tb_lineno))
            finally:
                # 在这里可以根据 title 进行个性化处理
                # 在一个 状态修改
                # url 可以在装饰器参数中添加 或者在 async_to_php 使用全局变量也行
                async_to_php(message_dict, url="", logger=logger)

        return pick

    return decorator
