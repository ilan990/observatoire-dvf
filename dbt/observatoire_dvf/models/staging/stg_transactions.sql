{{ config(materialized='table') }}

SELECT
    id,
date_mutation,
valeur_fonciere,
code_commune,
code_departement,
commune,
nature_mutation,
type_local,
surface_reelle_bati,
surface_terrain,
nombre_pieces_principales
FROM {{ source('raw', 'raw_dvf') }}
WHERE is_valid = true