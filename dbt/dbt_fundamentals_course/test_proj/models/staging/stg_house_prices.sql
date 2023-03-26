{{
    config(
        materialized='table'
    )
}}

with stg_house_prices AS (
    SELECT
        *
    FROM house_prices
)

SELECT * FROM house_prices