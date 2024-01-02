from logger_settings.logger import console
from pkg.decorator.base_decorator import check_out_param
from pkg.base_class.param_class import Param
from .app_public import user_create
from .param_dict import param as param_dict
from .tasks import user_handle_sync_


# 同步调用
@check_out_param(Param, param_dict, console)  # 参数校验
def user_handle_get(*args, **kwargs):
    console.debug("------------------------真正得到函数调用-------------------------")
    console.debug(kwargs)
    # 这里要判断是否需要通过判断参数检验是否通过来继续下面的参数
    # 当前 check_out_param 已经在参数不合法的情况下直接返回了

    # console.log(request.GET)
    return user_create(**kwargs)


# 异步调用
@check_out_param(Param, param_dict, console)  # 参数校验
def user_handle_post(*args, **kwargs):
    user_handle_sync_.delay(**kwargs)
    return {"code": 200, "errmsg": "处理中。。。。"}


@check_out_param(Param, param_dict, console)  # 参数校验
def user_handle_put(*args, **kwargs):
    console.debug(kwargs)
    return kwargs


@check_out_param(Param, param_dict, console)  # 参数校验
def user_handle_delete(*args, **kwargs):
    console.debug(kwargs)
    return kwargs
