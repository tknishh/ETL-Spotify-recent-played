import extract
import transform
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = 'sqlite:///my_played_tracks.sqlite'


if __name__ = "__main__":
    load_df = extract.return_dataframe()
    if(Transform.Data_quality(load_df)==False):
        raise("Failed at Data Validation")

    Transformed_df = Transform.Transformed_df(load_df)


    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor

    sql_query_1 = """
    CREATE TABLE IF NOT EXIST my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    sql_query_2 = """
    CRAETE TABLE IF NOT EXIST fav_artist(
        timestamp VARCHAR(200),
        ID VARCHAR(200),
        artist_name VARCHAR(200),
        count VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (ID)
    )
    """

    cursor.execute(sql_query_1)
    cursor.execute(sql_query_2)
    print("Opened database successfully")

    try:
        load_df.to_sql('my_played_tracks',engine, index=False, if_exists='append')
    except:
        print("Data already exists in db")

    try:
        Transformed_df.to_sql('fav_artist', engine, index=False, if_exists='append')
    except:
        print("Data already exists in db")

    conn.close()
    print("Close Database Successfully")