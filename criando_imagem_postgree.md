# Criado uma imagem de postgree

Create a postgres docker image with user 'student' password 'student'.


Crie um  Dockerfile

```{sql}
FROM postgres
ENV POSTGRES_PASSWORD postgres 
COPY init.sql /docker-entrypoint-initdb.d/
```

<br>

Crie um com as informações do banco   init.sql file

```{sql}
DROP DATABASE IF EXISTS sparkify;
CREATE DATABASE sparkify;

CREATE USER henry
WITH SUPERUSER PASSWORD '1234';

GRANT ALL PRIVILEGES ON DATABASE sparkify TO henry;
```

<br>

Crie os arquivos  **Dockerfile** e **init.sql** e execute a imagem no host 

```{bash}
docker build -t postgres-student .

docker run -d --name postgres-student -p 5432:5432 postgres-student
```

<br>

## Crie a imagem e realize o push para o docker hub  

Login

```{bash}
docker login docker.io
```

<br>

Build image and tag with docker username for relative path

```{bash}
docker build -t postgres-student-image .
docker tag postgres-student-image onekenken/postgres-student-image
docker login docker.io
docker push onekenken/postgres-student-image
```

<br>

Pull and run from docker hub retrieved image

```{bash}
docker pull onekenken/postgres-student-image

docker run -d --name postgres-student-container -p 5432:5432 onekenken/

postgres-student-image
```

<br>

[Image at docker hub](https://hub.docker.com/r/onekenken/postgres-student-image) address.

<br>

To rinse and repeat

```{bash}
docker stop postgres-student-container
docker rm postgres-student-container
docker rmi postgres-student-image
```
