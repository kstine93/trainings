# Intro to dbt:

**Resources:**
- [Intro to DBT video](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=introduction+to+dbt+fishtown#fpstate=ive&vld=cid:0fa75c93,vid:M8oi7nSaWps)
- [DBT Blog: Analytics Engineering](https://www.getdbt.com/what-is-analytics-engineering/)

---

## Introduction:
'Data build tool' tries to address data modeling issues with 2 principles:
- anyone who knows SQL can author their own data pipelines
- dbt + SQL allows others to work like data engineers (version control, test, documentation, re-usability)

## Core concepts of dbt:

### Express transforms exclusively with SQL `SELECT` statements
```
{{ config(materialized=table) }}

SELECT *
FROM public.orders
WHERE is.deleted = false
```
runs as:
```
CREATE TABLE analytics.orders AS (
    SELECT *
    FROM public.orders
    WHERE is.deleted = false 
);
```

This is a 'materialization' strategy, and dbt can make them for tables, views, CTEs, as well as for selective DB rebuilds ("incremental" it's called in dbt)


### Automatically build DAGs with `ref`s
`{{ ref(... )}}` handles dependencies in dbt models.
1. It interpolates the name of your schema
2. It builds an edge in the DAG between 2 models, helping dbt understand dependencies
```
SELECT * FROM {{ ref('MODEL_NAME') }}
```

With this, we can just change the 'ref' (like a config) as a way to change between development and production databases.
>Note: These `{{ }}` brackets are just jinja templating


### Build tests to ensure model accuracy
You write test assumptions in a YAML file. These assumptions get compiled into SQL that returns failing records.
Out of the box, dbt tests if a column:
- is unique
- doesn't contain nulls
- only contains certain values
- is a foreign key to another table

You can test anything that can be written as a query.
```
#schema.yaml
version: 2

models:
    - name: people
      columns:
        - name: id
          tests:
            - not_null
                severity: warn
            - unique
                severity: error
            - relationships:
                to: ref('accounts')
                field: id
                severity: error
```

### Documentation is accessible and easily updated
dbt generates documentation from your code and config files, including:
- model dependencies
- model SQL
- sources
- tests


### Use Macros + Jinja templating to write reusable SQL
- Use control structures (e.g., if statements, for loops) in SQL
- Use environment variables
```
{% macro cents_to_dollars(column_name, precision=2) %}
    ({{ column_name }} / 100)::numeric(16, {{ precision }})
{% endmacro %}


SELECT
    id AS payment_id
    ,{{ cents_to_dollars('amount') }} as amount_usd
    from app_data.payments
```

