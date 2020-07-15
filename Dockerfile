FROM alpine:latest

RUN echo "http://mirror.leaseweb.com/alpine/edge/community" >> /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

RUN apk add --no-cache --update \
	python3 py3-pip bash cmake gcc libxml2 \
	automake g++ subversion python3-dev \
	libxml2-dev libxslt-dev lapack-dev gfortran geos libc-dev musl-dev

ADD ./requirements.txt /tmp/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

ADD ./app /opt/app/
WORKDIR /opt/app

RUN adduser -D testuser
USER testuser

# EXPOSE 5000
# CMD ["python3", "main.py"]
CMD python3 main.py $PORT