# Criado uma imagem de postgree


Crie um  Dockerfile

```{sql}
FROM postgres
ENV POSTGRES_PASSWORD postgres 
COPY init.sql /docker-entrypoint-initdb.d/
```

<br>

Crie um arquivo init.sql com as informações do banco    

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

docker run -d --name postgres-servidor -p 5432:5432 postgres-student
```

<br>

## Realizando o login ao docker hub e criando a imagem  

Login

```{bash}
docker login docker.io
```

<br>

Criado a imagem 

```{bash}
docker build -t postgres-student .
docker tag postgres-student henrysilva/postgres-student
docker login docker.io
docker push henrysilva/postgres-student
```

<br>

Pull e run a partir do docker hub 

```{bash}
docker pull henrysilva/postgres-student

docker run -d --name postgres-servidor -p 5432:5432 henrysilva/postgres-student

```

<br>

[Image at docker hub](https://hub.docker.com/repository/docker/henrysilva/postgres-student) address.

<br>

Para pausar ou remover o container 

```{bash}
docker stop postgres-student-container
docker rm postgres-student-container
docker rmi postgres-student-image
```
