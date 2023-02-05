import pandas as pandas
import requests
from datetime import datetime
import datetime

USER_ID = 'c3drys7oy7f88tijr6fs0eg0i'
TOKEN = "BQANiNkEA-0Yk_j_LuyZp5wCuuBeWPgyUS3hWYJdhp9Yml-Tssct71L4BfD6pZ_BnY3DaT8sf1EJrY1vQ2Ofti0X59-5c6od4mdOyDM8RYqkN_uYA9P0CarWthUYOGk8C8Ow4B8Ktd4BLKONRh-KJXG0ADBh-0F089QtZ30pGUb_zvYsqflwmWgueDSMs9uJkot5ImVrow"

def return_dataframe(): 
    input_variables = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
     
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1) # no of Days u want the data for
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(time=yesterday_unix_timestamp), headers = input_variables)

    data = r.json()
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
        
    # Prepare a dictionary in order to turn it into a pandas dataframe below       
    song_dict = {
        "song_name" : song_names,
        "artist_name": artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }
    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
    return song_df