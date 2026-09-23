import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard IoT",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ Dashboard de Temperaturas - IoT")
st.write("Visualização dos dados de temperatura coletados pelos dispositivos IoT.")

# Conexão com o PostgreSQL
DB_URL = "postgresql+psycopg2://iot_user:iot_senha@localhost:5432/iot_database"
engine = create_engine(DB_URL)


# Função para carregar os dados das views
def carregar_dados(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)


# Carregar as três views
df_ambiente = carregar_dados("avg_temp_por_ambiente")
df_leituras = carregar_dados("leituras_por_dia")
df_temperaturas = carregar_dados("temp_max_min_por_dia")


# Indicadores
col1, col2, col3 = st.columns(3)

col1.metric(
    "Temperatura média",
    f"{df_ambiente['avg_temperature'].mean():.2f} °C"
)

col2.metric(
    "Total de leituras",
    f"{df_leituras['quantidade_leituras'].sum():,}"
)

col3.metric(
    "Maior temperatura",
    f"{df_temperaturas['temp_max'].max()} °C"
)


st.divider()


# Gráfico 1 - Média de temperatura por ambiente
st.subheader("🌡️ Média de temperatura por ambiente")

fig1 = px.bar(
    df_ambiente,
    x="room_id",
    y="avg_temperature",
    labels={
        "room_id": "Ambiente",
        "avg_temperature": "Temperatura média (°C)"
    }
)

st.plotly_chart(fig1, use_container_width=True)


# Gráfico 2 - Quantidade de leituras por dia
st.subheader("📊 Quantidade de leituras por dia")

fig2 = px.line(
    df_leituras,
    x="data",
    y="quantidade_leituras",
    labels={
        "data": "Data",
        "quantidade_leituras": "Quantidade de leituras"
    }
)

st.plotly_chart(fig2, use_container_width=True)


# Gráfico 3 - Temperatura máxima e mínima por dia
st.subheader("🌡️ Temperaturas máxima e mínima por dia")

fig3 = px.line(
    df_temperaturas,
    x="data",
    y=["temp_max", "temp_min"],
    labels={
        "data": "Data",
        "value": "Temperatura (°C)",
        "variable": "Tipo"
    }
)

st.plotly_chart(fig3, use_container_width=True)