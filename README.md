# Airflow DBT Docker Compose Example

This project demonstrates how to integrate DBT (Data Build Tool) with Apache Airflow using Docker Compose. It includes a sample DBT project and an Airflow DAG that runs DBT commands.

## Project Structure

- `dags/`: Contains Airflow DAG files
  - `dbt_example_dag.py`: A sample DAG that runs DBT commands
- `dbt_project/`: Contains the DBT project files
  - `dbt_project.yml`: DBT project configuration
  - `profiles.yml`: DBT connection profiles
  - `models/`: Contains DBT models
    - `example/`: Example models
      - `sample_model.sql`: A sample DBT model
      - `schema.yml`: Documentation for the sample model
- `docker-compose.yaml`: Docker Compose configuration for Airflow
- `.env`: Environment variables for Docker Compose
- `requirements.txt`: Python dependencies

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone this repository
2. Start the Docker Compose environment:

```bash
docker-compose up -d
```

3. Access the Airflow web interface at http://localhost:8080 (username: airflow, password: airflow)
4. Enable the `dbt_example` DAG to run the DBT commands

## How It Works

The sample DBT project creates a simple view based on the `information_schema.tables` in the PostgreSQL database. The Airflow DAG runs the following DBT commands:

1. `dbt debug`: Checks if DBT can connect to the database
2. `dbt compile`: Compiles the SQL but doesn't run it
3. `dbt run`: Runs the models
4. `dbt test`: Runs tests on the models
5. `dbt docs generate`: Generates documentation for the models

## Customizing

To customize this project for your own use:

1. Modify the DBT models in `dbt_project/models/`
2. Update the DBT project configuration in `dbt_project/dbt_project.yml`
3. Update the database connection in `dbt_project/profiles.yml`
4. Modify the Airflow DAG in `dags/dbt_example_dag.py`

## Additional Resources

- [DBT Documentation](https://docs.getdbt.com/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)