from django.http import JsonResponse, QueryDict
from django.views import View
from .handle_func import user_handle_get, user_handle_post, user_handle_put, user_handle_delete


# Create your views here.

class User(View):
    def get(self, request, *args, **kwargs):
        # print(request.GET)
        # print(dir(request))
        # 获取get 请求的 json 数据
        # print(json.loads(request.body.decode('utf-8')))

        # 获取对象的方法
        # methods = [method for method in dir(request) if callable(getattr(request, method))]
        # print(methods)
        data = user_handle_get(self, request, args, kwargs=kwargs)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # 请求的 context-type  设置为 form-data 或者 x-www-form-urlencoded 都可以用 request.POST 方式进行接收
        print(request.POST)
        # 获取 json 方式的数据
        # print(eval(request.body.decode('utf-8')))  # 这样就直接变成dict()
        data = user_handle_post(self, request, args, kwargs=kwargs)
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # 请求的 context-type  设置为 application/x-www-form-urlencoded;charset=utf-8
        print(QueryDict(request.body))

        return JsonResponse(user_handle_delete(self, request, args, kwargs=kwargs))

    def put(self, request, *args, **kwargs):
        print(QueryDict(request.body))
        # 请求的 context-type  设置为 application/x-www-form-urlencoded;charset=utf-8
        return JsonResponse(user_handle_put(self, request, args, kwargs=kwargs))
