import pandas as pd

def treat_df(df):
    df = df.sort_values(by='published_dates')
    df['order'] = df.index
    #corrgindo tipo de dado das coluna
    df["views"] = pd.to_numeric(df["views"])
    df["likes"] = pd.to_numeric(df["likes"])
    df["comments"] = pd.to_numeric(df["comments"])
    df['durations'] = df['durations'].apply(to_seconds)

    #Colunas de media movel
    window_size = 3
    min_window_size = 1
    df["comments_moving_avg"] = df["comments"].rolling(window=window_size, min_periods=min_window_size).mean()
    df["likes_moving_avg"] = df["likes"].rolling(window=window_size, min_periods=min_window_size).mean()
    df["views_moving_avg"] = df["views"].rolling(window=window_size, min_periods=min_window_size).mean()

    #Coluna de engajamento likes+coments/views
    df['engagements'] = (df["likes"]+df["comments"])/df["views"]

    #Coluna de locais
    df['places'] = df['titles'].replace(r'Race Highlights \| 2024 ', '', regex=True)
    df['places'] = df['places'].str.replace(r' Grand Prix', '', regex=True)

    #Colunas normalizadas
    df['normalized_views'] = (df['views'] - df['views'].min()) / (df['views'].max() - df['views'].min())
    df['normalized_likes'] = (df['likes'] - df['likes'].min()) / (df['likes'].max() - df['likes'].min())
    df['normalized_comments'] = (df['comments'] - df['comments'].min()) / (df['comments'].max() - df['comments'].min())

    #Coluna de Relevancia
    df['relevances'] = df['views'] + df['likes'] + df['comments']

    #Coluna de periodo (inicio, meio ou fim da temporada)
    

    return df

def to_seconds(string):
    if "M" in string:
        minutes = string.split("M")[0].replace("PT", "")
        seconds = string.split("M")[1].replace("S", "")
    else:
        mintuos = 0
        seconds = string.replace("PT", "").replace("S", "")
    return int(minutes) * 60 + int(seconds)