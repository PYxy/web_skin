import json, requests
import time

from django.http import QueryDict


def param_change(requests):
    """
       # 同时满足GET/POST/PUT/DELETE请求,请注意参数方式的限制
       :param requests:   request请求对象
       :return:
       """
    # method_type = None
    # get 请求不接收request body 参数
    if requests.method == "GET":
        # uri 参数
        method_type = requests.GET
    elif requests.method == "POST":
        # context-type  设置为 form-data 或者 x-www-form-urlencoded
        method_type = requests.POST
    elif requests.method in ["PUT", "DELETE"]:
        # application/x-www-form-urlencoded;charset=utf-8
        method_type = QueryDict(requests.body, encoding='utf')
    else:
        method_type = "请求类型异常"
    # 正常是一种<QueryDict: {'xxx': ['xxx']}>结构
    # 异常时一个字符串类型
    return method_type


def async_to_php(data, url, logger):
    """
    异步响应
    :param data:  请求数据
    :param url:   请求url
    :param logger: 日志对象
    :return:
    """
    try:
        logger.debug(f"异步任务结果:{data} 发送到:{url}")
        # response = requests.post(url, data)
        # # 如果请求php失败 需要将信息添加到表中
        # logger.debug(response.text)
    except Exception as e:
        logger.error(f'line(async_to_php)>> {str(e.__traceback__.tb_lineno)} => {str(e)}')
