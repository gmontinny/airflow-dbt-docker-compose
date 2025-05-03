FROM apache/airflow:2.9.1-python3.10

USER root
# Instalar pacotes básicos necessários para construção de bibliotecas e compilações
RUN apt-get update && apt-get install -y \
   git \
   build-essential \
   libssl-dev \
   libffi-dev \
   python3-dev

# Copiar os requirements
COPY requirements.txt /requirements.txt

# Alternar para o usuário airflow para instalar pacotes
USER airflow
RUN pip install --upgrade pip setuptools wheel && \
   pip install -r /requirements.txt && \
   chmod +x /home/airflow/.local/bin/dbt

# Ajustar permissões adicionais necessárias
USER root
RUN echo "export PATH=\$PATH:/home/airflow/.local/bin" >> /home/airflow/.bashrc
RUN mkdir -p /opt/airflow/dbt_project && chown -R airflow:root /opt/airflow/dbt_project

USER airflow
