FROM python:3.7.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip
ADD . /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt
RUN pip install gunicorn
RUN apk update && apk add libpq gcc binutils libc-dev
EXPOSE 5000
CMD ["gunicorn", "--bind","0.0.0.0:5000", "server:app"]
#CMD ["python3", "server.py", "-h 0.0.0.0"]
