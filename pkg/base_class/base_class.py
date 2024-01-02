# BaseView 视图继承类
import re


class BaseView:
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in ['get', 'post', 'put', 'patch', 'delete']:  # 将get post 请求 全部转为post 请求
            ret = self.handle(request, *args, **kwargs)
        else:
            # logger_p.error('**********************非法请求***********************************')
            ret = super(BaseView, self).http_method_not_allowed(request, *args, **kwargs)
        return ret


# BaseCheck 检查类
class BaseCheck:
    def __init__(self, function_name, check_param, param_dict, logger):
        self.key = 200
        self.debug = logger.debug
        self.error = logger.error
        self.param_return = dict()
        self.function_ = function_name
        self.check_param = check_param
        self.err = ""
        # 前端传的参数
        self.param_dict = param_dict  # 赋值调用

    # 用于检测逻辑返回的结果交给后面 来判断是否继续下去
    def up_(self):
        return {"code": self.key, 'errmsg': self.err}

    @property
    def param_dict(self):
        return self.param_dict_

    @param_dict.setter
    def param_dict(self, value):
        self.param_dict_ = value
        # print("方法调用:", value)

        # 这样写就变成了 每个url 都需要写一个检测方法
        # getattr(self, self.function_)()

        # 这个只需要继承的类写一个 check 方法就行
        getattr(self, "check")(self.check_param)

    def check(self, check_param):
        assert 0, "请编写正确的check 函数"


# 自定义字典类
class CheckDict(dict):

    def check_up(self, param_dict, logger):
        args = []
        code = 1
        for key in self.keys():
            if key in self.keys():
                try:
                    func = self.get(key)["function"]
                    args = self.get(key)["param"]

                    args.append(param_dict[key])
                    # 方法调用
                    func(*args)
                except Exception as e:
                    code = 0
                    logger(
                        f'line(check_up)>>> {str(e.__traceback__.tb_lineno)} => 参数合法性检测异常 [{key}]:{param_dict[key]}, '
                        f'function:[{func}] args:{args}')
                    return code, "参数异常"
                finally:
                    # 删除之前添加的检测元素
                    args.pop()
        return code, "参数合法检测通过"


# 参数合法性检测类
class ParamLegitimacy:

    @staticmethod
    def c_pattern(pat, target):
        """
        正则查询
        @param pat: 正则表达式
        @param target:  目标字符串

        """
        # print(f"正则检测 ：{target}   {pat}---------------------------------")
        assert re.search(pat, target).group() == target

    @staticmethod
    def c_limit(limit, target):
        """
        检查参数是不是在 某个范围内的
        :param args:
        :return:
        """
        # print(f"范围检测[范围:{limit} 被检测值:{target}]")

        assert target in limit

    @staticmethod
    def lazy_to_do(args):
        #  这个函数就是不校验参数合法性
        pass
