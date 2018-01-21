FROM meeting-base:0.1.1
MAINTAINER chenlin002@dragonest.com
ADD . /www
WORKDIR /www
RUN pip install -i https://pypi.doubanio.com/simple/ -r /www/requirements.txt
RUN pip install -i https://pypi.doubanio.com/simple/ uwsgi
RUN chmod a+x /www/entrypoint.sh
ENTRYPOINT ["/www/entrypoint.sh"]