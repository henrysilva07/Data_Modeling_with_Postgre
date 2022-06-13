FROM postgres
ENV POSTGRES_PASSWORD postegres
copy ini.sql /docker-entrypoint-initdb.d/
