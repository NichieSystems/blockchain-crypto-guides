FROM python:3.6-alpine

ENV FLASK_APP scurdex.py
ENV FLASK_CONFIG docker
ENV SCURDEX_ADMIN scurdex@protonmail.com

ENV SECRET_KEY de337cd67c737aec6c0a83f59813cf8176877c26e8aff5ce3601c925c2bac
ENV MAIL_SERVER email-smtp.us-east-1.amazonaws.com
ENV MAIL_PORT 465
ENV MAIL_USE_TLS yes
ENV MAIL_USERNAME AKIAUXN635JPBLUR2J7X
ENV MAIL_PASSWORD BB8K0egLizBP+mzYm/OH2YdYid3Lmf5PDN+rpexjCg+f
ENV DATABASE_URL postgresql://postgres:Zirac@223@localhost/scurdexdb

#  RUN adduser -D scurdex
#  USER scurdex

WORKDIR /home/server

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY scurdex.py config.py ./
COPY boot.sh ./

# run-time configuration
EXPOSE 5000
RUN chmod +x boot.sh
ENTRYPOINT ["./boot.sh"]

# ENV PORT 8080

# CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 scurdex:app
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 scurdex:app
# CMD [ "python","scurdex.py"]
# CMD ["./boot.sh"]


