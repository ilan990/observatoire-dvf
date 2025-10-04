-- depends_on: {{ ref('stg_transactions') }}

{{ config(materialized='table') }}

SELECT 
    code_commune,
    MAX(commune) as commune,
    MAX(code_departement) as code_departement
FROM {{ ref('stg_transactions') }}
GROUP BY code_commune