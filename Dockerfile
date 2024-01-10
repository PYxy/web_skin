FROM python:3.6.8-slim-stretch
RUN echo -e http://mirrors.ustc.edu.cn/alpine/v3.6/main/ > /etc/apk/repositories
RUN apk add --no-cache gcc musl-dev linux-headers

RUN mkdir /etc/python_file
COPY ./ ./

RUN pip3 install -r requestments.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir /etc/python_file/supervisor_log && mkdir /etc/supervisord && touch /etc/supervisord/supervisord.conf && ln -s /etc/supervisord/supervisord.conf  /etc/


CMD ["python","--version"]
