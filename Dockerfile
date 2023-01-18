FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN useradd django && chown -R django /app
RUN apt-get update
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
USER django
