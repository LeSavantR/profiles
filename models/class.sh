#! /usr/bin/bash

docker pull node:lts-alpine3.16
# Levantar contenedor con proceso null
docker run --name contenedor -d ubuntu:img tail -f /dev/null

# Comandos dentro del contenedor
docker exec -it contenedor bash


# Image NGINX Maquina:Container
# proxy: nombre que le doy al contenedor.
# nginx: imagen que uso.
docker run -d --name proxy -p 8080:80 nginx
# f: Sigue el stdout, tail: Sigue solo los ultimos registros
docker logs -f proxy


# Bind Mounts
## Whitout
docker run -d --name db mongo
## Whit
docker run -d --name db -v "$(pwd)"/data:/data/db mongo


# Volumenes
docker volume ls
docker volume create dbdata
docker inspect Container
docker run -d --name db --mount src=dbdata,dst=/data/db mongo

# Copia de archivos, dentro y fuera del contenedor.
## No importa si el contenedor esta corriendo o no.
docker run --name contenedor -d ubuntu:img tail -f /dev/null
docker cp archivo.txt contenedor:/carpeta/copy.txt
docker cp contenedor:/carpeta/copy.txt localtesting/new_copy.txt

# Imagenes
docker images

## Dockerfile demo
FROM ubuntu:latest
RUN touch /usr/src/hola-platzi.txt

## Build Docker Image
docker build -t tag_image .

## Retaggear
docker tag old-image:old-tag new-image:new-tag

## Push Image
docker push image:tag

## Dockerfile
docker history image:tag


# Docker Network
docker network ls
docker network create --attachable nombre_de_red
docker network inspect nombre_de_red
docker network connect nombre_de_red contenedor


# Docker Compose
docker compose up -d
docker compose ps
docker compose logs
docker compose exec app bash      # <-- No hace falta colocar -it
docker compose down               # <-- Baja todo y borra las redes y contenedores.
docker compose build
docker compose build servicio_especifico
## Docker Compose .override.yaml


# Administración de Docker
docker container prune # elimina los contenedores apagados
docker rm -f "$(docker ps -aq)"
docker network prune
docker volume prune
docker system prune

## Docker Stop
docker stop container
docker ps -l
docker kill container


# Contenedores ejecutables
models/Dockerfile

