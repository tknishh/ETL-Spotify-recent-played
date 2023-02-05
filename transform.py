import extract
import pandas as pd

def Data_quality(load_df):
    if load_df.empty:
        print('No songs Extracted')

    if pd.Series(load_df['played_at']).isunique:
        pass
    else:
        raise Exception("Primary Key Exception,Data Might Contain duplicates")

    if load_df.isnull().values.any():
        raise Exception("Null values found")

def Transform_df(load_df):
    Transformed_df = load_df.groupby(['timestamp','artist_name'], as_index = False).count()
    Transformed_df.RENAME(COLUMNS = {'played_at':'count'}, inplace = True)

    Transformed_df['ID'] = Transformed_df['timestamp'].astype(str) + "-" + Transformed_df['artist_name']

    return Transformed_df[['ID','timestamp','artist_name','count']]

if __name__ == "__main__":
    load_df = extract.return_dataframe()