import os
import pandas as pd
import json
import youtube_API

filePath = 'app/dados/highlights2024.json'

def save_playlistInfo(df):
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    objJson = df.to_dict(orient='dict')
    with open(filePath, 'w', encoding="utf-8") as f:
         json.dump(objJson,  f, ensure_ascii=False)

def get_playlistInfo():
    try:
        with open(filePath, 'r', encoding="utf-8") as f:
            objJson = json.load(f)
            df = pd.DataFrame(objJson)
            if df.empty:
                raise ValueError("O DataFrame está vazio.")
            else:
                return df
    except FileNotFoundError as e:
        df = youtube_API.get_ApiResponse()
        save_playlistInfo(df=df)
        return df
    except ValueError as e:
        df = youtube_API.get_ApiResponse()
        save_playlistInfo(df=df)
        return df
    
 
    
df = get_playlistInfo()
print(df)