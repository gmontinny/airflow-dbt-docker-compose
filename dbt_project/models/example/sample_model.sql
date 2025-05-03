/*
    This is a sample DBT model that creates a simple view.
    In a real project, this would typically transform data from a source table.
    Since we're using the Airflow database, we'll create a simple view based on information_schema.
*/

{{ config(
    materialized='view'
) }}

SELECT 
    table_name,
    table_schema,
    'This is a sample DBT model' as description
FROM 
    information_schema.tables
WHERE 
    table_schema = 'public'