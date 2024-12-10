import pandas as pd
import plotly.graph_objects as go
import data_manager

df = data_manager.get_playlistInfo()

#metrica de engajamento likes+coments/views
df_engagement = pd.DataFrame()
df_engagement['engagement'] = df['engagement']
df_engagement['title'] = df['title'].replace(r'Race Highlights \| 2024 ', '', regex=True)
df_engagement['title'] = df_engagement['title'].str.replace(r' Grand Prix', '', regex=True)
df_engagement = df_engagement.sort_values(by='engagement')

top_five_engagement = list(df_engagement['title'].tail(5))

#matriz de correalação entre view, likes e comentarios
matriz_corr = df[['comments', 'likes', 'views']].corr()

#grafico de linha da media de view, likes e comentarios
fig_moving_avg = go.Figure()
fig_moving_avg.add_trace(go.Scatter(
    x=df['order'],  
    y=df['views_moving_avg'],
    mode="lines+markers",                          
    name="Vizualizações"                                  
))
fig_moving_avg.update_layout(
    title="Media",
    xaxis_title="Tempo",
)
