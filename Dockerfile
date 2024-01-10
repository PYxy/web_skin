FROM python:3.6
COPY ./ ./

RUN pip install -r  requestments.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir /etc/python_file && mkdir /etc/python_file/supervisor_log && mkdir /etc/supervisord && touch /etc/supervisord/supervisord.conf && ln -s /etc/supervisord/supervisord.conf  /etc/


CMD ["python","--version"]
