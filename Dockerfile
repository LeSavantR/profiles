FROM python:3.10.6-alpine3.16

WORKDIR /build/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3.10", "manage.py", "runserver", "0.0.0.0:8000" ]