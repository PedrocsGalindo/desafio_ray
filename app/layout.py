from dash import html, dcc
import plots

layout = html.Div(children=[
    html.H1(children='Highlights da Temporada de Fórmula 1 - 2024'),
    html.Button('Atualizar', id='update_infos'),
    html.Div(children=[

        dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_engagement'),
        dcc.Graph(id="graph_bars_top_engagement",figure=plots.fig_bar_top_engagement),

        dcc.Graph(id="graph_bars_periods",figure=plots.fig_bar_periods),

        dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_means'),
        dcc.Graph(id="graph_mult_lines", figure=plots.fig_moving_avg)
    ])
])