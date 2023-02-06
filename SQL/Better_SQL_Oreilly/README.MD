# Writing Better SQL
O'Reilly Training
Feb. 6, 2023

---

## General Tips
- Focus on minimum viable product, then improve
- Break big operations into smaller pieces
  - You can use CTEs (`WITH`) or subqueries, or create temp tables or views to execute your query in multiple, smaller steps
- Take only the data that you need
  - Use `LIMIT`
  - Don't take all the columns - only those you need
  - Avoid expensive operations
    - `DISTINCT`
    - Using wildcards (e.g., LIKE `%@gmail`)
- Make your own execution plan on paper - to make sure you're only getting what you need - and in the right order
- First reduce volume of data, then operate
  - Filter the crap out of it to only get what you need



#### Example: Refactoring UNION
```
--Combining two tables:
SELECT * FROM customers
UNION
SELECT * FROM employees
```

Refactoring #1: if we use "UNION ALL" - we don't filter out duplicates:
```
--Combining two tables w/o removing duplicates:
SELECT * FROM customers
UNION ALL
SELECT * FROM employees
```
UNION stacks data, sorts it, and then removes duplicates
UNION ALL only stacks data

> Note: Often SQL editors will have an option of looking at the 'execution plan' which shows you how the query is actually being done - **and what takes more time**

---

#### How the interpreter runs your code:
The interpreter will take your SQL and interpret it in this order:
1. FROM (get tables and join as needed)
2. WHERE (filter)
3. GROUP BY (including aggregations)
4. HAVING
5. SELECT
6. ORDER BY

---

#### Example: Refactoring with subquery or CTE
```
--This query groups baby names by state
SELECT
    sd.state, bn.year, bn.name,
    SUM(bn.num_babies) AS total
FROM baby_name bn
    LEFT JOIN state_details sd
    ON bn.state = sd.abbreviation
WHERE year BETWEEN 1990 AND 1999
GROUP BY sd.state, bn.year, bn.name
ORDER BY total DESC;
```

By using a CTE or a subquery, this query can be made faster.
This is because we can filter down the table within the `FROM` statement
before we ever `JOIN`
```
--Subquery version (we could also build a CTE with "WITH")
SELECT sd.state, bn.year, bn.name,
    total
FROM (SELECT state, year, name) AS bn
    FROM baby_names
    WHERE year BETWEEN 1990 and 1999
    GROUP BY state, year, name
    ) AS bn
    LEFT JOIN state_details sd
    ON bn.state = sd.abbreviation
ORDER BY total DESC;
```

---

## Using Indexes
Let's say for 5 million rows, a query like `select * from table where name = "Dave"` takes ~50ms. when 'name' is indexed, it takes 20ms.

An index in SQL works similarly to a book index - showing you which 'pages' a particular value appears on.

> TIP: Indexes work better when there is low cardinality (only a few unique values)

Creating an index:
```
CREATE name_index ON table (name);

--Postgres: Check which columns are indexed:
SELECT indexname, indexdef
FROM pg_indexes
WHERE table_name = table
```

> TIP: **WHERE** and/or **JOIN** on indexed columns - these are expensive operations which can benefit most from indexes

> TIP: Use `IN` rather than chaining `AND` in `WHERE` when using indexes
