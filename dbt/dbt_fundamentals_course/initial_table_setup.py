import psycopg2
from psycopg2 import sql
import csv

#find postgres container ID:
postgres_docker_container = '70cd5e4b4530'

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


    # file = open('./house_prices.csv')
    # contents = file.read()
    # contents_arr = contents.splitlines()
    # db_cur.execute(f"INSERT INTO house_prices VALUES ({contents_arr[1]})")
    
    # # Converting string to dict:
    # dict_arr = [json.loads(val) for val in contents_arr]

    # # filter by NextSong action
    # next_song_logs = [log for log in dict_arr if log['page'] == "NextSong"]

    # # convert timestamp column to datetime
    # for log in next_song_logs:
    #     log['ts'] = datetime.datetime.fromtimestamp(log['ts']/1000) #Converting from ms
    
    # insert_into_time(cur,next_song_logs)
    # insert_into_users(cur,next_song_logs)
    # insert_into_songplays(cur,next_song_logs)




    # copy_command = "\copy fifa_winners FROM \'/home/rambino/dev/trainings/dbt/dbt_fundamentals_course/FIFA_award_winners.csv\' delimiter \',\' csv header"
    # print(f"docker exec -it {postgres_docker_container} psql -U postgres dbt_practice -c '{copy_command}'")
    # os.system(f"docker exec -it {postgres_docker_container} psql -U postgres dbt_practice -c '{copy_command}'")
    # db_cur.execute('''
    #     COPY fifa_winners(
    #         key_id
    #         ,tourn_id
    #         ,tourn_name
    #         ,award_id
    #         ,award_name
    #         ,shared
    #         ,player_id
    #         ,l_name
    #         ,f_name
    #         ,team_id
    #         ,team_name
    #         ,team_code
    #     )
    #     FROM './FIFA_award_winners.csv'
    #     DELIMITER ','
    #     CSV HEADER;
    # ''')
    db_conn.commit()