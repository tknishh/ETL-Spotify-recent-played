import extract
import pandas as pd

def Data_quality(load_df):
    if load_df.empty:
        print('No songs Extracted')

    if pd.Series(load_df['played_at']).isunique:
        pass
    else:
        raise Exception("Primary Key Exception,Data Might Contain duplicates")

        