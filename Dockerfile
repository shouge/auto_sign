FROM python:alpine3.18
MAINTAINER "Shou Ge <shouge101@gmail.com>"
RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
WORKDIR /opt
RUN git clone https://github.com/shouge/auto_sign.git && cd auto_sign
RUN pip --no-cache-dir install --upgrade pip && pip --no-cache-dir install -r requirements.txt
CMD ["python", "main.py"]