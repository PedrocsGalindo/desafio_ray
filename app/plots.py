import pandas as pd
import plotly.graph_objects as go
import data_manager

df = data_manager.get_playlistInfo()

print(df[['relevances', 'places']])

#grafico de barras com top 5 com mais engajamento
df_plot_engagement = df[['places','views','likes','comments', 'engagements']].copy()
df_plot_engagement = df_plot_engagement.sort_values(by='engagements', ascending=False)
df_plot_engagement = df_plot_engagement[:5]
fig_bar_top_engagement = go.Figure()

fig_bar_top_engagement.add_trace(go.Bar(
    y=df_plot_engagement['places'],
    x=df_plot_engagement['views'],
    marker_color='yellow',
    orientation='h'
))
fig_bar_top_engagement.update_layout(
    title='Top 5 Engajamentos',
)

def change_fig_bar(columns):
    fig_bar_top_engagement.data[-1].x = df[columns]
    return fig_bar_top_engagement


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

