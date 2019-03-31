FROM ubuntu:18.04

RUN apt-get update

RUN apt-get -y install nginx

COPY website /var/www

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
