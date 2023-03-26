/*
Query to split "State + Zip" and "country" columns and make it into a 2-column dimension table
*/

{{
    config(
        materialized='table'
    )
}}

with state_zip_country AS (
    SELECT
        SPLIT_PART(statezip,' ',1) AS state
        ,SPLIT_PART(statezip,' ',2) AS zipcode
        ,country
    FROM {{ ref('stg_house_prices') }}
)

SELECT * FROM state_zip_country