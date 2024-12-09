from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime
import requests
import data_treat

#acessando a chave da api
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")
if not api_key:
    print("Erro: Chave não encontrada no .env")

youtube = build('youtube', 'v3', developerKey=api_key)
playlist_id = 'PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR'

#retorna o dataframe, contendo as informações
def get_ApiResponse():
    playlist_videos = []
    stats = []

    views=[]
    likes=[]
    comments=[]
    titles=[]
    published_dates=[]
    duration=[]

    try:   
        #resposta API
        res = youtube.playlistItems().list(part='snippet', playlistId=playlist_id, maxResults=23).execute()
        playlist_videos = res['items']
        #titulos e ids dos videos
        video_ids_tittles = dict(
            map(lambda x: (x["snippet"]["resourceId"]["videoId"], {'title' : x["snippet"]["title"], 'published_date' : x["snippet"]["publishedAt"]}), playlist_videos)
        )
        #estatisticas dos videos
        for video in video_ids_tittles.keys():
            res = youtube.videos().list(part=['statistics','contentDetails'], id=video).execute()
            stats += (res['items'])

        #separando as estatisticas e informações
        for video in stats:
            titles.append(video_ids_tittles[video['id']]['title'])
            published_dates.append(video_ids_tittles[video['id']]['published_date'])
            views.append(video['statistics']['viewCount'])
            likes.append(video['statistics']['likeCount'])
            comments.append(video['statistics']['commentCount'])
            duration.append(video['contentDetails']['duration'])

    
        #transformando em um dataframe
        df = pd.DataFrame({
            'title': titles,
            'published_date' : published_dates,
            'extraction_date': None,
            'views' : views,
            'likes' : likes,
            'comments' : comments,
            'duration': duration
            })
        df['extraction_date'] = str(datetime.now())

        #tratar os dados
        return data_treat.treat_df(df)

    except HttpError as e:
        print(f"Erro HTTP: {e}")

    except requests.ConnectionError:
        print("Erro de conexão: Sem acesso à internet.")

df = get_ApiResponse()