FROM python:3.11-alpine3.16

RUN apk add gcc g++ cmake make mupdf-dev freetype-dev

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ["requirements.txt", "."]

# RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY [".", "."]

RUN python3 manage.py makemigrations app profiles
# RUN python3 manage.py migrate
# RUN python3 manage.py collectstatic

EXPOSE 8000

CMD [ "gunicorn", "core.wsgi", "--bind", "0.0.0.0:8000" ]
