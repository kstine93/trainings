# DBT Fundamentals Course

From https://courses.getdbt.com/courses/take/fundamentals/lessons/

**Resources:**
- https://docs.getdbt.com/

---

## Where dbt fits into the data flow
dbt is for **transforming** your data once it is loaded into your data platform (e.g., Redshift, BigQuery, Snowflake).
<img src="./media/dbt_workflow.png">

---

## How does dbt work?
dbt is just using SQL `SELECT` queries to define transformations and the creation of new tables. dbt then uses these queries to understand the relationships and dependencies between tables - and builds a DAG for you.
You can then set up a scheduler (via most any tool I think, but also dbt cloud - the paid service) to activate the pipeline.

## dbt commands
```
#Run your data pipeline
> dbt run

#Run the tests you've defined for your data pipeline
> dbt test

#Run AND Test:
> dbt build

#Generate dbt documentation page:
> dbt docs generate
```

