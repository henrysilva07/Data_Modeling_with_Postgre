# Modelagem de dados com Postgre

Neste projeto, iremos criar um banco de dados no postgre `sparkifydb` para o aplicativo de música, Sparkify. O objetivo é modelar o conjunto de dados presentes nos arquivos *Song_data*, que presenta as músicas executadas e nos arquivos *Log_data*, que indica os artistas e as músicas presentes no aplicativo. O schema de dados utilizado foi o star schema para otimizar as queries analíticas. 

# Designer do schema e ETL pipeline 

O schema star possui uma tabela fato (songplays)  e 4 tabelas de dimensões (songs, users, artists, time). `Drop', `ĆREATE`, `ÌNSERT' e `SELECT`queries são definidas em `sql_queries.py`. **Create_tables.py** utiliza as funções `create_databse` , `drop_tables`e  `create_tables` para criar o banco de dados sparifydb e suas tabelas. 


