FROM python:3.6
ADD . /www
WORKDIR /www
RUN pip install -i https://pypi.doubanio.com/simple/ -r /www/requirements.txt
RUN chmod a+x entrypoint.sh
ENTRYPOINT ["/www/entrypoint.sh"]