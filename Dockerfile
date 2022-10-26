FROM python:3.10.6-alpine3.16

WORKDIR /usr/src/app

COPY ["requirements.txt", "/usr/src/app/"]

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY [".", "/usr/src/app/"]

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
