import psycopg2 
import os 
import glob 
import pandas as pd



"""import psycopg2

# Conectando ao servidor postgres
conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkify user=henry password=1234")
conn.set_session(autocommit=True)

print(" CONEXÃO BEM SUCEDIDA") """

import glob , os 
import pandas as pd
filepath = 'data/song_data'

all_data = []
for pasta , subpasta , arquivo in os.walk(filepath):

        
        arquivos = glob.glob(os.path.join(pasta, '*.json'))
        for f in arquivos:
                all_data.append(os.path.abspath(f))
        num_arquivos = len(all_data)
print(all_data[0])

df = pd.read_json(all_data[0],lines = True)

print(df)
        


teste = list(df[['song_id', 'title', 'artist_id', 'year','duration']])
print(teste)