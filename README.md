# Projeto: Modelagem de dados com Postgre

## Motivação do Projeto

Uma startup chamada Sparkify deseja analizar os dados coletados sobre as músicas executadas e os usuários ativos em seu aplicativo de streaming de músicas. Entretanto eles não possuem conhecimento acerca de manipulação de dados, que estão presentes em arquivos JSON.

Eles necessitam de um engenheiro de dados para criar um ambiente OLAP que permita a otimização de queries analíticas para que seja possível realizar uma análise exploratória desses dados, bem como para fornecer os dados de uma maneira estruturada para os analistas da empresa. Dito isso, cabe ao engenheiro de dados desenvolver toda a insfraestrutura necessária para o ambiente e o pipeline de dados. 

## Descrição do Projeto 

Este projeto será realizado em três passos:
  * Criação de um banco Postgree utilizado Docker que será nosso servidor;
  * Criação de todas as tabelas necessárias para a modelagem do negócio;
  * Realização do pipeline de dados para carga dos dados.


# Designer do schema

O banco utilizado para realizar o armazenamento dos dados será um *Postgre* que será criado via docker. O nosso banco irá priorizar queries analícas, por tanto, foi definido que a melhor opção seria criar o nosso modelo utilizando um star schema. 

O nosso star schema possui uma tabela fato (songplays)  e 4 tabelas de dimensões (songs, users, artists, time). `Drop`, `CREATE`, `INSERT` e `SELECT`queries são definidas em `sql_queries.py`. **Create_tables.py** utiliza as funções `create_databse` , `drop_tables`e  `create_tables` para criar o banco de dados sparifydb e suas tabelas. Na imagem abaixo, é possível visualizar como ficou os relacionamentos entre nossas dimensões e a fato.

![](diagrama/sparkifydb.png)

# Definição do ETL 

O nosso pipeline foi realizado por meio da linguagem python. O processo de Extração,transformação e carga acontece por meio do script **etl.py**. Nas tabelas **artist** e **songs** são inseridos os dados presentes nos arquivos `data/song_data`. Por outro lado, o arquivo json `data/log_file`é utilizado para realizar a carga dos dados nas tabelas **time**, **users** e , por fim, a tabela **songsplays** é preenchida com base em informações de ambos arquivos, formando então nossa tabela fato. 


# Criando o container com o docker 

Para não precisar instalar o postgree em minha máquina, eu criei um container utilizando docker. Utilizei a imagem **postgres-student** que criei especificamente para esse projeto.

Para realizar o download da imagem, instale o docker , crie um login e uma senha. No terminal, realize-se o login docker hub (via terminal)

```
docker login docker .io
```
Pull da imagem do container 
```
docker pull henrysilva/postgres-student
```
Inicializando o container 

```
docker run -d --name postgres-servidor -p 5432:5432 henrysilva/postgres-student
```
A conecão com o container pode ser realizar por meio dos seguintes parâmetros: 
`conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=henry password=1234")`

Para pausar ou remover o container

```
docker stop  postgres-servidor

docker rm  postgres-servidor
```
# Ordem de execução dos arquivos:

Cria-se o servidor utilizando docker, depois é necessário realizar a criação das tabelas (**create_tables.py**) e por fim executa o arquivo **elt.py**
