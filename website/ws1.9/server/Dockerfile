FROM python:3.6

RUN pip install flask gunicorn firebase_admin flask-mail flask-login flask-pagedown flask-sqlalchemy flask-wtf flask-bootstrap flask-moment

COPY app/ app/

WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 scurdex:app