from .base_class import BaseCheck


# model_dict = {
#     "user": "app01",
# }


# 按照不同的参数导入不同的包去进行参数校验
# class ParamV1(BaseCheck):
#     # 通用的检测方法
#     def check(self, model_dict=None):
#         # 获取参数字典以及对应的检查方法
#         try:
#             self.debug(f"参数列表:{self.function_}:{self.param_dict_}")
#             # self.debug(f"key:{sys._getframe().f_code.co_name}")
#             # 获取当前方法的 方法名
#             # check_dict = param[sys._getframe().f_code.co_name]
#             # param_list = param[sys._getframe().f_code.co_name].keys()
#
#
#             # 动态导入模块
#             # model_patch = importlib.import_module(f"{model_dict['app_name']}.param_dict")
#             # check_dict = model_patch.param.get(self.function_)
#             # param_list = model_patch.param.get(self.function_).keys()
#             self.debug(f"参数检测字典:{check_dict},需要获取的参数:{param_list}")
#             # 获取参数值
#             param_dict = dict(
#                 zip(param_list,
#                     [self.param_dict.get(x, None).strip() for x in param_list])
#             )
#             self.debug(param_dict)
#             # 参数校验
#             code, errmsg = check_dict.check_up(param_dict)
#             assert code, errmsg
#             self.debug("参数获取成功,且合法性检验通过")
#         except Exception as e:
#             self.error('line>>>' + str(e.__traceback__.tb_lineno))
#             self.key, self.err = 0, str(e)
#             self.param_return = self.up_()
#         finally:
#             # 下面的字段按需添加就行 这里是模拟 异步任务需要回传task_id
#             self.param_return.update({"task_id": self.param_dict.get('task_id')}) if "task_id" in self.param_dict else 0
#
#     # 这样写就变成了 每个url 都需要写一个检测方法
#     def create(self):
#         # 获取参数字典以及对应的检查方法
#         try:
#             self.debug(f"参数列表:{self.function_}:{self.param_dict_}")
#             self.debug(f"key:{sys._getframe().f_code.co_name}")
#             # 获取当前方法的 方法名
#             check_dict = param[sys._getframe().f_code.co_name]
#             param_list = param[sys._getframe().f_code.co_name].keys()
#
#             self.debug(f"参数检测字典:{check_dict},需要获取的参数:{param_list}")
#             # 获取参数值
#             param_dict = dict(
#                 zip(param_list,
#                     [self.param_dict.get(x, None).strip() for x in param_list])
#             )
#             self.debug(param_dict)
#             # 参数校验
#             code, errmsg = check_dict.check_up(param_dict)
#             assert code, errmsg
#             self.debug("参数获取成功,且合法性检验通过")
#         except Exception as e:
#             self.error('line>>>' + str(e.__traceback__.tb_lineno))
#             self.key, self.err = 0, str(e)
#             self.param_return = self.up_()
#         finally:
#             # 下面的字段按需添加就行 这里是模拟 异步任务需要回传task_id
#             self.param_return.update({"task_id": self.param_dict.get('task_id')}) if "task_id" in self.param_dict else 0


class Param(BaseCheck):
    # 通用的检测方法 找父类 BaseCheck 的check 方法
    def check(self, param_dict):
        """
        :param param_dict: 每个App 中 的 param_dict.py 中 的 param 参数
        :return:
        """
        # 获取参数字典以及对应的检查方法
        try:
            self.debug(self.function_)
            # param_dict 中没有定义该请求方法的校验参数
            check_dict = param_dict.get(self.function_)
            if check_dict is None:
                self.param_return = {"code": 200, 'errmsg': ""}
                return
            # 用户定义的必须要获取到的参数列表
            param_list = param_dict.get(self.function_).keys()
            self.debug(f"参数检测字典:{check_dict},需要获取的参数:{param_list}")
            # 获取参数值,如果前端没有传 默认为 "" 空字符串
            param_dict = dict(
                zip(param_list,
                    [self.param_dict.get(x, "").strip() for x in param_list])
            )
            self.debug(f"获取到的前端参数:{param_dict}")
            # 参数校验
            code, errmsg = check_dict.check_up(param_dict, self.error)
            assert code, errmsg
            # 把参数校验的结果 封装在param_return 然后传递下去
            self.param_return = self.up_()
            # 参数透传给后面的处理函数
            self.param_return.update(param_dict)
            self.debug("参数获取成功,且合法性检验通过")
        except Exception as e:
            self.key, self.err = 0, str(e)
            self.error(f'line(Param.check)>>> {str(e.__traceback__.tb_lineno)} {str(e)}')
            self.param_return = self.up_()
