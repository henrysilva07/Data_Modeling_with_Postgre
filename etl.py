import psycopg2 
import os 
import glob 
import pandas as pd
from sql_queries import *


def processando_song_file(cur, filepath):
    """ Esta função processa os dados brutos song_file

    Parâmetros:
    -----------
    cur: cursor do banco de dados   
    filepath: str , caminho do arquivo 
    """

    # Abrindo o arquivo song_file
    df = pd.read_json(filepath , lines = True)

    # Inserindo os dados na dimensão songs 
    song_data = list(df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0])

    cur.execute(song_table_insert ,song_data)

    # Inserindo os dados na dimensão artists
    artista_df = list(df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 
                        'artist_longitude']].values[0])

    cur.execute(artist_table_insert , artista_df)


def processando_log_file(cur , filepath):
    """Esta função processa os dados brutos log_file
    
    Parâmetros:
    -----------
    cur: cursor do banco de dados   
    filepath: str , caminho do arquivo 
    """

    # Abrindo o arquivo
    df = pd.read_json(filepath, lines=True)

    # filtrando por  NextSong 
    df = df[df['page'] == 'NextSong']

    # Convertendo timestamp  para datetime
    time = pd.to_datetime(df['ts'], unit='ms')

    # Inserindo dados 
    time_data = [
        df.ts.values, time.dt.hour.values, time.dt.day.values, time.dt.isocalendar().week, 
                time.dt.month.values, time.dt.year.values, time.dt.weekday.values
                ]

    colunas = [
        'start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday'
    ]
    
    time_df = pd.DataFrame(dict(zip(colunas , time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index , row in df.iterrows():
    # Buscando o songid e artist_id a partir das tabelas song e artistas
    
        cur.execute(song_select , (row.song , row.artist , row.length))
        result = cur.fetchone()
    
    
        print(result)
    
        if result:
            songid, artistid = result 
        else:
            songid, artistid = None , None 
        
        # insert songplay record
        songplay_data = [row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent]
    
        cur.execute(songplay_table_insert, songplay_data)
        

    

def processando_dados( cur, conn , caminho , func):

    """Esta função processa os dados  de música

    Parâmetros:
    -----------
    cur : cursor do banco de dados
    conn: conector do banco de dados
    caminho : str, caminho dos dados
    func: função que processará os dados de cada caminho

    """


    # Coletando o diretório dos arquivos json
    all_data = []
    for pasta , subpasta , arquivo in os.walk(caminho):
        arquivos = glob.glob(os.path.join(pasta, '*.json'))
        for arq in arquivos:
            all_data.append(os.path.abspath(arq))
    num_arquivos = len(all_data)

    
    print(f"O número de arquivos: {num_arquivos} encontrados no caminho: {caminho}")

    for i , datafile in enumerate(all_data,1):
        func(cur, datafile)
        conn.commit()
        print(f"{i}/{num_arquivos} arquivos processos")




def main():

    # Criando a conexão ao banco 
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=henry password=1234")

    # Criando cursor
    cur = conn.cursor()

    print(" Conexão ao banco realizada com sucesso")

    processando_dados(cur, conn, caminho='data/song_data', func=processando_song_file)
    processando_dados(cur, conn, caminho='data/log_data', func = processando_log_file)


    

if __name__ == "__main__":
    main()