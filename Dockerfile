FROM ubuntu:14.04.3

MAINTAINER codemeow codemeow@yahoo.com

RUN cp /etc/apt/sources.list /etc/apt/sources.list.raw
ADD https://github.com/codemeow5/software/raw/master/ubt_sources_list_aliyun.txt /etc/apt/sources.list
RUN apt-get update && apt-get install wget -y

RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python-pip python-dev -y
RUN apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
	libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk -y
RUN pip install django
RUN pip install MySQL-python
RUN pip install qrcode
RUN pip install Pillow
RUN pip install openpyxl

EXPOSE 80

RUN echo Asia/Shanghai > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN mkdir /FreeSpoon
COPY / /FreeSpoon/
WORKDIR /FreeSpoon

#RUN python manage.py migrate
#CMD /usr/bin/python manage.py runserver 0.0.0.0:80

ENTRYPOINT /bin/bash ./wait-for-it.sh db:3306 -- python manage.py migrate && \
		/bin/bash load_data.sh && \
		python manage.py runserver 0.0.0.0:80