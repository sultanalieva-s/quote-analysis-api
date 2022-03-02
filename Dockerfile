FROM python:3
LABEL maintainer="saadatssu@gmail.com"
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ./manage.py makemigrations && ./manage.py migrate