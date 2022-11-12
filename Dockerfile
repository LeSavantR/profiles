FROM python:3.11-alpine3.16

RUN apk add gcc g++ cmake make mupdf-dev freetype-dev

WORKDIR /usr/src/app

COPY ["requirements.txt", "."]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY [".", "."]

RUN python3 manage.py makemigrations app profiles
# RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

EXPOSE 8000

CMD [ "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000" ]
