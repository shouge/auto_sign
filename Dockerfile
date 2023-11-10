FROM python:alpine3.18
MAINTAINER "Shou Ge <shouge101@gmail.com>"
RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
WORKDIR /opt
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]