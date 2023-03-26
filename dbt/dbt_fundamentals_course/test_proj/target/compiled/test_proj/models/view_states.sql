/*
practice view to just see how 'ref' works
*/

WITH states AS (
    SELECT
        state
    FROM "dbt_practice"."public"."dim_states_zip"
)

SELECT * FROM states