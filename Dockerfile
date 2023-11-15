FROM python:alpine3.18
MAINTAINER "Shou Ge <shouge101@gmail.com>"
RUN apk add tzdata && apk add git && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
RUN git clone https://github.com/shouge/auto_sign.git /opt/auto_sign
WORKDIR /opt/auto_sign
RUN pip --no-cache-dir install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]