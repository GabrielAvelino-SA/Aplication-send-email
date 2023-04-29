FROM postgres:14.4

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD mysecretpassword
ENV POSTGRES_DB mydatabase
ENV PGPORT=5432

EXPOSE 5432

COPY /database/db.sql /docker-entrypoint-initdb.d/
RUN apt-get update

# RUN mkdir -p /home/db
# COPY ./database/db.sql /home/db

# RUN mkdir -p /scripts