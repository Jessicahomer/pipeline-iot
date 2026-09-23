import pandas as pd
from sqlalchemy import create_engine

# Caminho do arquivo CSV
CSV_PATH = "data/IOT-temp.csv"

# Dados de conexão com o PostgreSQL
DB_URL = "postgresql+psycopg2://iot_user:iot_senha@localhost:5432/iot_database"

# Ler o CSV
df = pd.read_csv(CSV_PATH)

# Renomear as colunas para nomes mais fáceis de trabalhar
df = df.rename(columns={
    "id": "id",
    "room_id/id": "room_id",
    "noted_date": "noted_date",
    "temp": "temperature",
    "out/in": "location"
})

# Converter a data para o formato correto
df["noted_date"] = pd.to_datetime(
    df["noted_date"],
    format="%d-%m-%Y %H:%M"
)

# Criar conexão com o PostgreSQL
engine = create_engine(DB_URL)

# Enviar os dados para o PostgreSQL
df.to_sql(
    "temperature_readings",
    engine,
    if_exists="replace",
    index=False
)

print(f"{len(df)} registros inseridos com sucesso!")