FROM python:3.11-alpine3.16

WORKDIR /usr/src/app

COPY ["requirements.txt", "."]

RUN apk add gcc g++ cmake make mupdf-dev freetype-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY [".", "."]

RUN python3 manage.py makemigrations app profiles
# RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
