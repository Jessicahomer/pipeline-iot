# Pipeline de Dados com IoT e Docker

Projeto desenvolvido para a disciplina de Disruptive Architectures: IoT, Big Data e IA.

O projeto apresenta um pipeline de dados capaz de processar leituras de temperatura de dispositivos IoT, armazenar os dados em PostgreSQL utilizando Docker e apresentar os resultados em um dashboard interativo com Streamlit e Plotly.

## Tecnologias utilizadas

- Python
- Pandas
- PostgreSQL
- Docker
- SQLAlchemy
- psycopg2
- Streamlit
- Plotly
- Git e GitHub

## Dataset

Foi utilizado o dataset **Temperature Readings: IoT Devices**, disponibilizado pelo Kaggle.

O arquivo utilizado no projeto é:

`data/IOT-temp.csv`

O dataset possui **97.606 registros** de leituras de temperatura.

## Estrutura do projeto

```text
pipeline-iot/
├── data/
│   └── IOT-temp.csv
├── docs/
├── sql/
│   └── views.sql
├── src/
│   ├── dashboard.py
│   └── etl.py
├── .gitignore
└── README.md

## Funcionamento do pipeline

O funcionamento do projeto segue as seguintes etapas:

1. O dataset CSV é lido utilizando Python e Pandas.
2. Os dados são tratados e as colunas são renomeadas.
3. A coluna de data é convertida para o formato adequado.
4. Os dados são enviados para um banco PostgreSQL.
5. O PostgreSQL é executado em um container Docker.
6. São criadas três Views SQL para análise dos dados.
7. O Streamlit consulta as Views do banco.
8. O Plotly apresenta os dados em gráficos interativos.

## Banco de dados

O PostgreSQL é executado através do Docker.

Container:

`postgres-iot`

Banco de dados:

`iot_database`

Usuário:

`iot_user`

Tabela principal:

`temperature_readings`

## Views SQL

O projeto possui três Views:

### 1. Média de temperatura por ambiente

`avg_temp_por_ambiente`

Apresenta a temperatura média registrada em cada ambiente.

### 2. Quantidade de leituras por dia

`leituras_por_dia`

Apresenta a quantidade de registros de temperatura realizados em cada dia.

### 3. Temperaturas máxima e mínima por dia

`temp_max_min_por_dia`

Apresenta a maior e a menor temperatura registrada em cada dia.


## Dashboard

O dashboard foi desenvolvido utilizando Streamlit e Plotly.

Ele apresenta:

- Temperatura média;
- Total de leituras;
- Maior temperatura registrada;
- Média de temperatura por ambiente;
- Quantidade de leituras por dia;
- Temperaturas máxima e mínima por dia.

### Principais resultados

Durante a análise dos dados foram identificados:

- Temperatura média geral: **35,05 °C**
- Total de leituras: **97.606**
- Maior temperatura registrada: **51 °C**

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Jessicahomer/pipeline-iot.git
cd pipeline-iot

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate

### 3. Instalar as dependências

```bash
pip install pandas psycopg2-binary sqlalchemy streamlit plotly

### 4. Criar o container PostgreSQL

```bash
docker run --name postgres-iot \
-e POSTGRES_USER=iot_user \
-e POSTGRES_PASSWORD=iot_senha \
-e POSTGRES_DB=iot_database \
-p 5432:5432 \
-d postgres

### 5. Executar o ETL

```bash
python src/etl.py

### 6. Criar as Views SQL

```bash
docker exec -i postgres-iot psql -U iot_user -d iot_database < sql/views.sql

### 7. Executar o dashboard

```bash
streamlit run src/dashboard.py

## Conclusão

O projeto demonstra a utilização de tecnologias de IoT e análise de dados para coletar, armazenar, processar e visualizar informações de temperatura.

A utilização do Docker facilita a execução do banco PostgreSQL, enquanto Python, SQL, Streamlit e Plotly permitem realizar o processamento e a visualização dos dados.