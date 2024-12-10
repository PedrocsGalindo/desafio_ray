from dash import html, dcc
import plots

layout = html.Div(children=[
    html.H1(children='Highlights da Temporada de Fórmula 1 - 2024'),
    html.Button('Atualizar', id='update_infos'),
    html.Div(children=[

        dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='lista_medias'),
        dcc.Graph(
        id="grafico-multiplas-linhas",
        figure=plots.fig_moving_avg
        )
    ])
])