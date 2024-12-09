import pandas as pd

def treat_df(df):
    df = df.sort_values(by='published_date')
    df['order'] = df.index
    #corrgindo tipo de dado das coluna
    df["views"] = pd.to_numeric(df["views"])
    df["likes"] = pd.to_numeric(df["likes"])
    df["comments"] = pd.to_numeric(df["comments"])
    df['duration'] = df['duration'].apply(to_seconds)
    return df

def to_seconds(string):
    if "M" in string:
        minutes = string.split("M")[0].replace("PT", "")
        seconds = string.split("M")[1].replace("S", "")
    else:
        mintuos = 0
        seconds = string.replace("PT", "").replace("S", "")
    return int(minutes) * 60 + int(seconds)