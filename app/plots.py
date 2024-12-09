import pandas as pd
import plotly.graph_objects as go
import data_manager

df = data_manager.get_playlistInfo()

#metrica de engajamento likes+coments/views
#df['engagement'] = (df["likes"]+df["comments"])/df["views"]

print(df["views"])

#matriz de correalação entre view, likes e comentarios
matriz_corr = df[['comments', 'likes', 'views']].corr()



# grafico de linha da media de view, likes e comentarios
window_size = 3
min_window_size = 1
df["comments_moving_avg"] = df["comments"].rolling(window=window_size, min_periods=min_window_size).mean()
df["likes_moving_avg"] = df["likes"].rolling(window=window_size, min_periods=min_window_size).mean()
df["views_moving_avg"] = df["views"].rolling(window=window_size, min_periods=min_window_size).mean()
fig_moving_avg = go.Figure()

fig_moving_avg.add_trace(go.Scatter(
    x=df['order'],  
    y=df['views_moving_avg'],
    mode="lines+markers",                          
    name="Vizualizações"                                  
))
fig_moving_avg.add_trace(go.Scatter(
    x=df['order'],  
    y=df['likes_moving_avg'],
    mode="lines+markers",                          
    name="Curtidas",
    line=dict(color="red")                             
))
fig_moving_avg.add_trace(go.Scatter(
    x=df['order'],  
    y=df['comments_moving_avg'],
    mode="lines+markers",                          
    name="Comentarios",
    line=dict(color="yellow")                          
))
fig_moving_avg.update_layout(
    title="Media",
    xaxis_title="Ordem de vídeos",
)
