import pandas as pd

def treat_df(df):
    df = df.sort_values(by='published_date')
    df['order'] = df.index
    #corrgindo tipo de dado das coluna
    df["views"] = pd.to_numeric(df["views"])
    df["likes"] = pd.to_numeric(df["likes"])
    df["comments"] = pd.to_numeric(df["comments"])
    df['duration'] = df['duration'].apply(to_seconds)

    #Colunas de media movel
    window_size = 3
    min_window_size = 1
    df["comments_moving_avg"] = df["comments"].rolling(window=window_size, min_periods=min_window_size).mean()
    df["likes_moving_avg"] = df["likes"].rolling(window=window_size, min_periods=min_window_size).mean()
    df["views_moving_avg"] = df["views"].rolling(window=window_size, min_periods=min_window_size).mean()

    #Coluna de engajamento likes+coments/views
    df['engagement'] = (df["likes"]+df["comments"])/df["views"]

    return df

def to_seconds(string):
    if "M" in string:
        minutes = string.split("M")[0].replace("PT", "")
        seconds = string.split("M")[1].replace("S", "")
    else:
        mintuos = 0
        seconds = string.replace("PT", "").replace("S", "")
    return int(minutes) * 60 + int(seconds)