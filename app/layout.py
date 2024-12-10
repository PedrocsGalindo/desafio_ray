from dash import html, dcc
import plots

layout = html.Div(children=[
    html.Div(children=[
        html.H1(children='Highlights da Temporada de Fórmula 1 - 2024', className='title'),
        html.Button('Atualizar', id='update_infos', className='btn'),
        ], className='div'),
    html.Div(children=[
        html.Div(children=[
        html.Div(children=[
            dcc.Dropdown(['views', 'likes', 'comments'], value='views', id='list_engagement'),
            dcc.Graph(id="graph_bars_top_engagement", figure=plots.fig_bar_top_engagement),
        ], style={"flex": "1", "padding": "10px"}),  
        dcc.Graph(id="graph_bars_periods", figure=plots.fig_bar_periods, 
                  style={"flex": "1", "padding": "10px"}),  
    ], className='div'),
        dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_means'),
        dcc.Graph(id="graph_mult_lines", figure=plots.fig_moving_avg)
    ])
])