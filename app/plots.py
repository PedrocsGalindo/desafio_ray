import pandas as pd
import plotly.graph_objects as go
import data_manager
from datetime import datetime, timezone

df = data_manager.get_playlistInfo()
dicionario_cores = dicionario_cores = {
    'views': '#FFD700',  # Amarelo dourado
    'likes': '#FF6347',  # Vermelho tomate
    'comments': '#1E90FF'  # Azul profundo
}

# region Grafico de barras com os estatisticas da temporada
df_top_periods = df[['normalized_comments', 'normalized_likes', 'normalized_views','periods']].copy()
df_top_periods = df_top_periods.groupby('periods').sum()
row_to_move = df_top_periods.loc['end']
df_top_periods = df_top_periods.drop(index='end')
df_top_periods.loc['end'] = row_to_move

fig_bar_periods = go.Figure()
fig_bar_periods.add_trace(go.Bar(
    x=df_top_periods.index,
    y=df_top_periods['normalized_views'],
    marker_color=dicionario_cores['views'],  
    name="Vizualizações"
))
fig_bar_periods.add_trace(go.Bar(
    x=df_top_periods.index,
    y=df_top_periods['normalized_likes'],
    marker_color=dicionario_cores['likes'],  
    name="Curtidas"
))
fig_bar_periods.add_trace(go.Bar(
    x=df_top_periods.index,
    y=df_top_periods['normalized_comments'],
    marker_color=dicionario_cores['comments'],  
    name="Comentários"
))
fig_bar_periods.update_layout(
    title='Ao longo da Temporada',
    template="plotly_dark",
    paper_bgcolor='#1e1e2f',  
    plot_bgcolor='#1e1e2f',  
    height=380
)
#endregion

#region grafico de barras verticais de todos os videos
fig_bar_all = go.Figure()
fig_bar_all.add_trace(go.Bar(
    y=df['places'],            
    x=df['views'],
    orientation='h'
    )
)
fig_bar_all.update_layout(
    template="plotly_dark",
    paper_bgcolor='#1e1e2f',  
    plot_bgcolor='#1e1e2f', 
)
def change_fig_bar_all(column):
    df_aux = df[[column, 'places']]
    df_aux = df_aux.sort_values(by=column, ascending=True)
    fig_bar_all.data[-1].x = df_aux[column]
    fig_bar_all.data[-1].y = df_aux['places']
    return fig_bar_all
#endregion

# region Grafico de linha da media de view, likes e comentarios (necessario 30 dias)
df_mean = df[['comments_moving_avg', 'likes_moving_avg', 'views_moving_avg', 'order', 'published_dates', 'places']].copy()
df_mean['published_dates'] = pd.to_datetime(df_mean['published_dates'])
df_mean['posting_time'] = (datetime.now(timezone.utc) - df_mean['published_dates']).dt.days
df_mean = df_mean[df_mean['posting_time'] >= 30]

fig_moving_avg = go.Figure()
fig_moving_avg.add_trace(go.Scatter(
    x=df_mean['order'],
    y=df_mean['views_moving_avg'],
    mode="lines+markers",
    name="Vizualizações",
    line=dict(color=dicionario_cores['views']),
))
fig_moving_avg.update_layout(
    xaxis=dict(
        tickvals=df_mean['order'].tolist(),
        ticktext=df_mean['places'].tolist(),
        title="Tempo"
    ),
    template="plotly_dark",
    title="Media",
    paper_bgcolor='#1e1e2f',  
    plot_bgcolor='#1e1e2f',  
)
def change_fig_moving(columns):
    columns = columns +'_moving_avg'
    fig_moving_avg.data[-1].y = df_mean[columns]
    return fig_moving_avg
# endregion

# variaveis de KPIs
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

# region Lista top 5 engajamento e relevancia
df_aux = df[['relevances', 'engagements','places','likes','views','comments', 'titles']].copy()

df_tops_relevance = df_aux.sort_values(by='relevances', ascending=False)
df_tops_relevance = df_tops_relevance[0:5]

df_tops_engagement = df_aux.sort_values(by='engagements', ascending=False)
df_tops_engagement = df_tops_engagement[0:5]
#endregion