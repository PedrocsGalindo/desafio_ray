import pandas as pd
import plotly.graph_objects as go
import data_manager
from datetime import datetime, timezone

df = data_manager.get_playlistInfo()
dicionario_cores = {'views' : 'yellow', 'likes' : 'red', 'comments': 'blue'}

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
    fig_bar_top_engagement.data[0].marker.color = dicionario_cores[columns]
    return fig_bar_top_engagement

#grafico de barras com os estatisticas da temporada
df_top_periods = df[['normalized_comments', 'normalized_likes', 'normalized_views','periods']].copy()
df_top_periods = df_top_periods.groupby('periods').sum()
row_to_move = df_top_periods.loc['end']
df_top_periods = df_top_periods.drop(index='end')
df_top_periods.loc['end'] = row_to_move

fig_bar_periods = go.Figure()
fig_bar_periods.add_trace(go.Bar(
    x=df_top_periods.index,
    y=df_top_periods['normalized_views'],
    marker_color='yellow',
    name="Vizualizações" 
))
fig_bar_periods.add_trace(go.Bar(
    x=df_top_periods.index,
    y=df_top_periods['normalized_likes'],
    marker_color='red',
    name="Curtidas" 
))
fig_bar_periods.add_trace(go.Bar(
    x=df_top_periods.index,
    y=df_top_periods['normalized_comments'],
    marker_color='blue',
    name="Comentarios" 
))
fig_bar_periods.update_layout(
    title='Ao longo da Temporada',
    height=380
)

#grafico de pizza de todos os videos
fig_pizza = go.Figure()
fig_pizza.add_trace(go.Pie(
    labels=df['places'],            
    values=df['views'],
    hole=0.3)
)

#matriz de correalação entre view, likes e comentarios
matriz_corr = df[['comments', 'likes', 'views']].corr()

#grafico de linha da media de view, likes e comentarios (necessario 30 dias)
df_mean = df[['comments_moving_avg', 'likes_moving_avg', 'views_moving_avg', 'order', 'published_dates']].copy()
df_mean['published_dates'] = pd.to_datetime(df_mean['published_dates'])
df_mean['posting_time'] = (datetime.now(timezone.utc) - df_mean['published_dates']).dt.days
df_mean = df_mean[df_mean['posting_time'] >= 30]

fig_moving_avg = go.Figure()
fig_moving_avg.add_trace(go.Scatter(
    x=df_mean['order'],  
    y=df_mean['views_moving_avg'],
    mode="lines+markers",                          
    name="Vizualizações"                                  
))
fig_moving_avg.update_layout(
    title="Media",
    xaxis_title="Tempo",
)
def change_fig_moving(columns):
    columns = columns +'_moving_avg'
    fig_moving_avg.data[-1].y = df_mean[columns]
    return fig_moving_avg

#variaveis de KPIs
dict_func = {
    'mean': pd.Series.mean,
    'max' : pd.Series.max,
    'min' : pd.Series.min,
    'sum' : pd.Series.sum
}
def kpis(column, func = 'mean'):
    if column == 'durations':
        value = int(dict_func[func](df[column]))
        answer = str(int(value/60)) + " min " + str(value % 60) + " seg"
    else:
        value = int(dict_func[func](df[column]))
        answer = str(int(value/1000)) + 'mil'
    if func == 'max' or func == 'min':
        local = df.loc[df[column] == value, 'places']
        local = local.iloc[0]
        answer = local +": " + answer
    return answer

#Lista top 5 engajamento e relevancia
df_aux = df[['relevances', 'engagements','places','likes','views','comments', 'titles']].copy()

df_tops_relevance = df_aux.sort_values(by='relevances', ascending=False)
df_tops_relevance = df_tops_relevance[0:5]

df_tops_engagement = df_aux.sort_values(by='engagements', ascending=False)
df_tops_engagement = df_tops_engagement[0:5]
