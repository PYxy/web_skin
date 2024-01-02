
### django web 统一参数校验

```text
重点 
1.每个app 中的 param_dict.py 文件

例如 app01 中的views.py 中定义了 User 类的 4中请求方法,
那 param_dict.py 中的 param 参数就分别定义了 每种请求方法中需要提供的参数 以及对应的检测方法

2.当前使用的数据库是 sqlite + redis(按需)


建议: 无论是不是必传的参数 都需要传,这样写起来方便,大不了用lazy_to_do,到真正使用的时候再检验




```


#### 运行说明
```text
当前测试所需模块(可能有遗漏 按需安装)
python                 3.7
django                 3.2.23
celery                 5.2.7
django-celery          3.3.1
django-celery-beat     1.5.0
redis                  5.0.1 
pyMySQL                1.1.1



cd  到 manage.py 的目录

如果需要运行celery 需要进行数据迁移才能测试,并且需要修改 celery_config.py 中的 BROKER_URL 和 CELERY_RESULT_BACKEND
python manage.py makemigrations 
python manage.py migrate

# 开启worker
celery -A web_skin worker -l info -P eventlet
# 监控定时任务
celery -A web_skin beat -l info -S django



如果只需要用到普通的web 请求(本例子中的 get put delete),post 是异步请求 用到了celery

python manage.py runserver 

使用postman  进行测试 ,观察日志就可以看明白数据的走向
请求参数怎么带,可以看app01中的views.py 中的说明
```

