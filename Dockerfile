FROM i.registry.dragonest.net/meeting-base:latest
MAINTAINER chenlin002@dragonest.com
ADD . /www
WORKDIR /www
RUN pip install -i https://pypi.doubanio.com/simple/ -r /www/requirements.txt
RUN pip install -i https://pypi.doubanio.com/simple/ uwsgi
RUN chmod a+x /www/entrypoint.sh
ENTRYPOINT ["/www/entrypoint.sh"]
