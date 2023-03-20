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
- Express transforms exclusively with SQL `SELECT` statements
- Automatically build DAGs with `ref`s
- Tests ensure model accuracy
- Documentation is accessible and easily updated
- Use Macros to write reusable SQL
