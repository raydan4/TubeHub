FROM python:3.7.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apk update && apk add libpq gcc binutils libc-dev
ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt
RUN pip install gunicorn
ADD . /usr/src/app/
EXPOSE 5000
CMD ["gunicorn", "--bind","0.0.0.0:5000", "server:app"]
#CMD ["python3", "server.py", "-h 0.0.0.0"]
