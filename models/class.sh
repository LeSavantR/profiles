#! /usr/bin/bash

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
docker run -d --name db mongo
