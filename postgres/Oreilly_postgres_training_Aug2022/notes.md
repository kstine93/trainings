# O'Reilly Postgres Training
Aug. 4, 2022
Presenter: Haki Benita

## Overview of Training
1. Manage users & permissions
2. Create & manage tables
3. Evaluate query performance
4. Create indexes to speed up performance
5. CLI commands (e.g., in psql)

## Notes
### Query Optimization
Once you submit a psql query, it is sent to the server and:
1. The parser checks for syntax errors
2. The query is rewritten as needed (inline views, etc.)
3. **A planner/optimizer produces an execution plan**
4. Executer executes the query according to the execution plan

The planner/optimizer is the big selling point of postgresql (apparently)

#### Query Optimizer
**Steps when optimizing for COST**
1. The optimizer generates all possible execution plans
   1. e.g., "scan entire table for specific user" or "use index table to find location of specific user"
2. For each execution plan, calculate **cost** of the plan (mostly impacted by I/O operations - lessened by indexing / partitioning)
3. Choose plan with lowest cost and forward to Executor

>We can use the 'Explain' command to return the execution plan
```
EXPLAIN SELECT * FROM my_table;

EXPLAIN (ANALYZE, TIMING) SELECT * FROM my_table;
```

>Exploration of execution plans:
```
EXPLAIN SELECT * FROM actor WHERE first_name = 'Bob';

 Seq Scan on actor  (cost=0.00..4.50 rows=1 width=25)
   Filter: ((first_name)::text = 'Bob'::text)
(2 rows)
```
This is planning a sequential scan on the 'actor' table.
It is estimating a number of rows to be '1'
returned between '0.00' and '4.50'.

### Using indexes to speed up query processing
Let's imagine that we often want to query our table of movies if they were produced after 2000 (modern movies being more popular). There are a few ways we can use INDEXES to speed up query performance

This is a **B-Tree Index**
```
CREATE INDEX movies_after_2000_index ON movies btree(year);
```
This is a **Partial Index** - only indexin the most important part of the table
```
CREATE INDEX movies_after_2000_partialindex ON movies (id) WHERE year >= 2000;
```
This is an **Inclusive Index** - it actually stores some value (in this case 'title') as PART of the index - so we don't have to query the table at all if we just want the title of movies.
Can however create very large indexes
```
CREATE UNIQUE INDEX movies_after_2000_inclusiveindex ON movies(key) INCLUDE (title);
```
This is a Function-based index. It allows us to index just based on a function (like Regex)
```
CREATE INDEX movies_after_2000_functionindex ON movies (substring(title FROM '.*://([^/]+)'));
```
This is a hash index. It's (apparently) helpful when values are "almost unique"
Can be smaller & faster than B-index, but has some restrictions on what operations it can support.
```
CREATE INDEX movies_after_2000_hashindex ON movies using HASH (year);
```
More types of indexes: **Block Index** and **BRIN Index**



### The Database administration system
DB admin ranges from basic details like operating system to high-level applications like dashboards:
- Infrastructure:
  - OS
  - Storage
  - Network
  - Installation
- Data Engineering / Admins
  - Data Modeling
  - Tables
  - Users
  - Indices
  - Performance
- Application
  - SQL
  - ORM
  - BI
  - Reporting
  - Dashboards

### Brief history of SQL
- Developed in 1970s at IBM, based on work by Edgar F. Codd
- Became standardized in 1986 (ANSI-86)
- Standard revised in 1992 (ANSI-92)

### Glossary & Terms
- Cluster = Postgres installation
  - Can contain multiple databases
  - Users & permissions managed on a cluster level
- Database = Designated storage area on file system
  - Contains DB objects (like tables)
- User = Granted permissions to operate on cluster
  - `show max_connections` - shows how many users can access postgres
- Shared Buffers (i.e., cache)
  - Keeps frequently-accessed objects in memory for fast retrieval
  - Shared by all cluster processes
  - Default = 128mb
  - `show shared_buffers` - shows shared buffers
- Memory
  - Used for sorts and hash tables
  - Default 1mb
  - `show work_mem`
- Temporary buffers
  - Used for storing temporary tables
  - `show temp_buffer`
- Maintenance working memory
  - Used for vaccum and create index operations
  - default 64mb
  - `show maintenance_work_mem`
- Write-ahead log (WAL)
  - Log of all changes made to tables and indexes
  - Used to restore database in case of failure
  - Can be used for replicating database & maintaining replicates
  - Enables point-in-time recovery

### Views
Views are named queries - they are not 'materialized' as full tables

### Schemas
Schemas are namespaces in the database

In every Postgres cluster, there is a schema called "pg_catalog" which has meta-information about the system. Also see:
- "pg_table"
- "pg_class"
- "pg_stat_activity"
- "pg_stat_all_table"
- "pg_stats"
- "pg_stat_all_indexes"

### Ensuring Data Integrity
- To better ensure data integrity, set as many constraints as possible, at low a level as possible

#### Column Types
First line of defense is **column types** - ensuring that data is not being inserted in the wrong place
```
INSERT INTO my_table (bool_col,varchar_col)
VALUES (t, "my_value")
```
**Special types**
- uuid
- jsonb
- range
- array
- etc...

#### Not Null Constraints
```
ALTER TABLE my_table ALTER bool_col SET NOT NULL
```

#### Primary Keys
- Must be unique by default
- Cannot be NULL by default
- Only 1 primary key per table (excepting composite keys)
  
"Identity" creates a sequence (it is replacing "Serial")
```
CREATE TABLE my_table (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT
)
```

#### Unique Constraints
```
ALTER TABLE my_table ADD CONSTRAINT mytable_name_unique
UNIQUE(name);
```
```
ALTER TABLE my_table DROP CONSTRAINT mytable_name_unique;
```

#### Check Constraints
>Note: it's quite important to set meaningful names to constraints - because this name is often the only specific error printed if constraints are violated.

>Note: You can also use check constraints as a more flexible way to enforce character limits
```
CREATE TABLE my_table (
  name text,
  CONSTRAINT name_length_check CHECK (length(name) > 20),
  name2 varchar(20)
)
```
```
ALTER TABLE my_table ADD CONSTRAINT must_contain_whitespace CHECK (name LIKE '% %');
```

#### Deleting data
```
ALTER TABLE my_table ADD CONSTRAINT my_foreignkey
FOREIGN KEY (user_id) REFERENCES users(id)
ON DELETE CASCADE

ON DELETE RESTRICT
```
>"ON DELETE CASCADE" - when a user is deleted from the users table, delete associated data in 'my_table'
>"ON DELETE RESTRICT" - When a user is deleted from the users table, do nothing.

---

### Commands (in psql)

#### Create Database
*Note: When referencing objects*
Basic command

`CREATE DATABASE my_db OWNER basic_user;`

Create DB from terminal

`createdb mydb -0 basic_user;`

Create table "my_table" within particular schema "my_schema"
```
CREATE TABLE my_schema.my_table
```

#### inspect database
`\d`

#### Inspect tables
`\dt`

#### Show or update search path of Postgres (for when you name objects ambiguously)
(Also look up "Synonyms" in PostgreSQL)
`SHOW search_path`
`SET search_path to my_schema, "$user", public;`

#### Alter Table
```
ALTER TABLE users ALTER COLUMN name SET DEFAULT "No Name";
```
### Create Views
```
CREATE VIEW active_users AS
  SELECT id, name
  FROM users
  WHERE active;
```

### Create Schemas
```
CREATE SCHEMA restricted;
```

### Inspect contents of CSV file
Note: '\!' is used to execute operating system instructions from inside psql
```
\! cat /filepath/file.csv
```

### Copy contents of CSV file INTO table
>Note on "Copy" command:
"Copy" executes on the server
"\Copy" executes on the client, provided by psql
(Only the server "Copy" command works with multiple lines in terminal. But if you use the server COPY like `COPY my_table TO STDOUT WITH CSV HEADER \g results.csv` (note \g), then the results of the query will be outputted to the client instead (this is a way to write multi-line copy commands but still get the reuslts locally)

```
\COPY my_table (col2, col1, col3) FROM /filepath/file.csv WITH CSV HEADER
```

### Export entire Postgres table to CSV file
```
\COPY my_table TO /tmp/all_users.csv WITH CSV HEADER;
```

### Export results of query to file
```
\COPY (SELECT col3 FROM my_table)TO /tmp/all_users.csv WITH CSV HEADER;
```

### CREATE USER
```
CREATE USER basic_user PASSWORD 'newpassword';
```
### Look at users table
```
\du
```

### Grant permissions to users
```
GRANT SELECT UPDATE INSERT ON my_table TO basic_user;
REVOKE SELECT UPDATE INSERT ON my_table FROM basic_user;
```

### CREATE ROLE
Roles are groups of permissions to be granted to certain types of users

```
CREATE ROLE analyst;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;

CREATE USER bob;
GRANT analyst TO bob;
```

Only grant access only to specific columns:
```
GRANT SELECT(user_id) ON my_table TO basic_user;
```

### Look up permissions
```
SELECT grantee, privilege_type
FROM information_schema.role_table_grants;
```

### Connect to Database
```
psql -d my_database -U basic_user -W
```
>-d = database name, -U = name of user, -W = prompt for password (more secure, no pws in logs)