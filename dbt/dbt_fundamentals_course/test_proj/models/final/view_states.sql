/*
practice view to just see how 'ref' works
*/

WITH states AS (
    SELECT
        state
    FROM {{ ref('dim_states_zip') }}
)

SELECT * FROM states
