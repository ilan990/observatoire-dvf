{{ config(materialized='table') }}

SELECT 
    s.id,
    s.date_mutation,
    s.valeur_fonciere,
    s.nature_mutation,
    s.type_local,
    s.surface_reelle_bati,
    s.surface_terrain,
    s.nombre_pieces_principales,
    s.code_commune,
    dc.commune,
    dc.code_departement
FROM {{ ref('stg_transactions') }} s
LEFT JOIN {{ ref('dim_communes') }} dc 
    ON s.code_commune = dc.code_commune