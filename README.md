# Exemplo de Integração Airflow DBT com Docker Compose

Este projeto demonstra como integrar o DBT (Data Build Tool) com o Apache Airflow utilizando Docker Compose. O projeto inclui um exemplo de projeto DBT e um DAG do Airflow que executa comandos DBT para orquestrar a transformação de dados.

## Sobre o Projeto

Este ambiente de desenvolvimento permite criar pipelines de dados completos, onde o Airflow orquestra a execução de transformações DBT. O DBT (Data Build Tool) é uma ferramenta moderna para transformação de dados que permite escrever transformações em SQL e gerenciar dependências, documentação e testes de forma eficiente. O Apache Airflow é uma plataforma de orquestração de fluxos de trabalho que permite programar, monitorar e gerenciar pipelines de dados complexos.

A integração dessas ferramentas proporciona:
- Orquestração confiável de transformações de dados
- Versionamento de código SQL
- Documentação automática
- Testes de qualidade de dados
- Monitoramento e alertas

## Estrutura do Projeto

- `dags/`: Contém os arquivos DAG do Airflow
  - `dbt_example_dag.py`: Um DAG de exemplo que executa comandos DBT
- `dbt_project/`: Contém os arquivos do projeto DBT
  - `dbt_project.yml`: Configuração do projeto DBT
  - `profiles.yml`: Perfis de conexão do DBT
  - `models/`: Contém os modelos DBT
    - `example/`: Modelos de exemplo
      - `sample_model.sql`: Um modelo DBT de exemplo
      - `schema.yml`: Documentação para o modelo de exemplo
- `docker-compose.yaml`: Configuração do Docker Compose para o Airflow
- `.env`: Variáveis de ambiente para o Docker Compose
- `requirements.txt`: Dependências Python
- `Dockerfile`: Configuração para construção da imagem Docker personalizada

## Pré-requisitos

- Docker
- Docker Compose

## Como Iniciar

1. Clone este repositório
2. Inicie o ambiente Docker Compose:

```bash
docker-compose up -d
```

3. Acesse a interface web do Airflow em http://localhost:8080 (usuário: airflow, senha: airflow)
4. Ative o DAG `dbt_example` para executar os comandos DBT

## Como Funciona

O projeto DBT de exemplo cria uma view simples baseada na tabela `information_schema.tables` no banco de dados PostgreSQL. O DAG do Airflow executa os seguintes comandos DBT:

1. `dbt debug`: Verifica se o DBT pode se conectar ao banco de dados
2. `dbt compile`: Compila o SQL mas não o executa
3. `dbt run`: Executa os modelos
4. `dbt test`: Executa testes nos modelos
5. `dbt docs generate`: Gera documentação para os modelos

## Personalização

Para personalizar este projeto para seu próprio uso:

1. Modifique os modelos DBT em `dbt_project/models/`
2. Atualize a configuração do projeto DBT em `dbt_project/dbt_project.yml`
3. Atualize a conexão com o banco de dados em `dbt_project/profiles.yml`
4. Modifique o DAG do Airflow em `dags/dbt_example_dag.py`

## Casos de Uso

Este projeto pode ser adaptado para diversos casos de uso, como:
- ETL/ELT para data warehouses
- Preparação de dados para análise
- Transformação de dados para dashboards
- Validação e testes de qualidade de dados

## Recursos Adicionais

- [Documentação do DBT](https://docs.getdbt.com/)
- [Documentação do Apache Airflow](https://airflow.apache.org/docs/)
