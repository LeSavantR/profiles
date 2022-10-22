FROM python:3.10.6-alpine3.16

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8001

CMD [ "python3.10", "manage.py", "runserver" ]