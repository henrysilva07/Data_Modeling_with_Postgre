from sql_queries import create_table_queries , drop_table_queries
import psycopg2






def criando_banco():
    
    # Criando a conexão ao banco 
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkify user=henry password=1234")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # Criando o database 
    cur.execute(" DROP DATABASE IF EXISTS  sparkifydb")
    cur.execute(" CREATE DATABASE sparkifydb WITH ENCODING 'utf-8' TEMPLATE template0")
    
    
    # Realizando o commit 
    conn.commit()

    # Fechando o banco padrão 
    conn.close()
    # Criando a conexão ao banco 
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=henry password=1234")
    cur = conn.cursor()


    return  conn , cur


def apagando_tabelas(conn, cur):

    for query in drop_table_queries:

        cur.execute(query)

    conn.commit()


    print(" Tabel Apagadas com Sucesso! \n")



def criando_tabelas(conn, cur):

    for query in create_table_queries:

        cur.execute(query)
    
    conn.commit()

    print(" Tabel Criadas com Sucesso! \n")



def main():

    conn ,cur = criando_banco()
    
    apagando_tabelas(conn, cur)

    criando_tabelas(conn, cur)

    conn.close()




if __name__ == "__main__":
    main()





