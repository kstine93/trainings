
  
    

  create  table "dbt_practice"."public"."stg_house_prices__dbt_tmp"
  as (
    

with stg_house_prices AS (
    SELECT
        *
    FROM house_prices
)

SELECT * FROM house_prices
  );
  