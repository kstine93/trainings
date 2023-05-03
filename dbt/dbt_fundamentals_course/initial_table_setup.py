import psycopg2
from psycopg2 import sql
import csv

#connecting to local postgres instance:
conn_dict = {
    'host':'localhost',
    'port':'5432',
    'dbname':'dbt_practice',
    'user':'postgres',
    'password':'postgres'
    }

db_conn = psycopg2.connect(**conn_dict)
db_cur = db_conn.cursor()


#Loading in local data on FIFA winners:
#db_cur.execute('DROP TABLE house_prices')
db_cur.execute('''
    CREATE TABLE IF NOT EXISTS house_prices(
        date DATE
        ,price NUMERIC(13,2)
        ,bedrooms NUMERIC(4,1)
        ,bathrooms NUMERIC(4,1)
        ,sqft_living INTEGER
        ,sqft_lot INTEGER
        ,floors NUMERIC(4,1)
        ,waterfront SMALLINT
        ,view SMALLINT
        ,condition SMALLINT
        ,sqft_above INTEGER
        ,sqft_below INTEGER
        ,yr_built SMALLINT
        ,yr_renovated SMALLINT
        ,street VARCHAR
        ,city VARCHAR
        ,statezip VARCHAR
        ,country VARCHAR
    )
''')
               
db_conn.commit()


db_cur.execute('''select * from house_prices LIMIT 5''')

result = db_cur.fetchall()

#If table has entries, just print entries:
if len(result) > 0:
    print(result)
else:
    with open('house_prices.csv', 'rt') as f:
        csv_reader = csv.reader(f)
        next(csv_reader) #Skipping header

        for line in csv_reader:
            #Repeating "%s" values to be replaced with values in 'line' array:
            query = sql.SQL(f"INSERT INTO house_prices VALUES ({','.join(['%s']*len(line))})")
            #print(query.as_string(db_conn))
            db_cur.execute(query,line)

    db_conn.commit()