# -*- coding: UTF-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse
from views_support import change, RSAUtils, SET_SSH
from Mysql_Administrator.settings import logger, SSH_USER, SSH_PWD, SSH_PORT
import json
from datetime import datetime, timedelta
from Mysql_Administrator.get_local_ip import get_ip


rsa = RSAUtils()


class MD1(MiddlewareMixin):
    def process_request(self, request):
        try:
            logger.debug("******************预处理*******************")
            method_type = change(request)
            if isinstance(method_type, dict):
                token = method_type.get("token", None).strip()
                try:
                    real_token = rsa.decrypt(token)
                    # print(real_token)
                except Exception as e:
                    logger.warning(str(e))
                    logger.error("line>>>>" + str(e.__traceback__.tb_lineno))
                    logger.warning("token不合法")
                    return HttpResponse(json.dumps({"code": 0, "errmsg": "参数不合法"}, ensure_ascii=False))
                    # 检验时间戳合法性
                now_time = datetime.now()
                now_stamp = datetime.timestamp(now_time)
                before_time = (datetime.now() - timedelta(minutes=3))
                datetime_stamp = datetime.timestamp(before_time)
                if int(datetime_stamp) <= int(real_token):
                    pass

                else:
                    return HttpResponse(json.dumps({"code": 0, "errmsg": "前参数不合法"}, ensure_ascii=False))
            else:
                return HttpResponse(json.dumps({"code": 0, "errmsg": "请求类型有误"}, ensure_ascii=False))
        except Exception as e:
            logger.warning(str(e))
            logger.warning("参数不合法")
            logger.error("line>>>>" + str(e.__traceback__.tb_lineno))
            return HttpResponse(json.dumps({"code": 0, "errmsg": "前参数不合法"}, ensure_ascii=False))