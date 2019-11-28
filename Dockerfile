FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./requirements.txt /app/app/requirements.txt

WORKDIR /app/app

RUN pip install -r requirements.txt

COPY ./app /app



