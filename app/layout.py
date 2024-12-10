from dash import html, dcc
import plots

layout = html.Div(children=[
    html.Div(children=[
        html.Header(children='Highlights da Temporada de Fórmula 1 - 2024', className='title'),
        html.Button('Atualizar', id='update_infos', className='btn'),
        ], 
        className='div'
    ),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id="graph_bars_periods", figure=plots.fig_bar_periods, 
                style={
                    "flex": "1", 
                }
            ),  
            html.Div(children=[
                    html.Div(children = [
                        html.Div(children=[
                            html.H2(children="KPI's", className=' title subtitle'),

                            html.Div(children=[
                                html.Div(children=[
                                    html.H3(children="vizualizações", className=' title subtitle minsubtitle'),
                                    html.P(children=plots.kpis('views'), id='kpis_views')
                                ], className='center'
                                ),
                                html.Div(children=[
                                    html.H3(children="curtidas", className=' title subtitle minsubtitle'),
                                    html.P(children=plots.kpis('likes'), id='kpis_likes')
                                ], className='center'
                                ),
                                html.Div(children=[
                                    html.H3(children="comentarios", className=' title subtitle minsubtitle'),
                                    html.P(children=plots.kpis('comments'), id='kpis_comments')
                                ], className='center'
                                ),
                                html.Div(children=[
                                    html.H3(children="Duração", className=' title subtitle minsubtitle'),
                                    html.P(children=plots.kpis('durations'), id='kpis_durations')
                                ], className='center'
                                ),
                            ], className='div mid_row'
                            ),
                            html.Div(children=[
                                dcc.RadioItems(id='radio_options_kpis', options=[
                                    {"label": "Media", "value": "mean"},
                                    {"label": "Maior", "value": "max"},
                                    {"label": "Menor", "value": "min"},
                                    {"label": "Soma", "value": "sum"}], 
                                    value="mean", 
                                    labelStyle={"display": "inline-block", "margin-right": "15px"}
                                    ),
                                ],
                                style = {
                                    "display": "flex",
                                    "gap": "10px",
                                    'justify-content': 'center', 
                                    'align-items': 'center'
                                }
                            )
                        ], 
                        className='grid-container grid_max_width'
                        )
                    ], 
                    className='grid_padding center'
                    ),
                ], 
                style={
                    "flex": "1", 
                    "padding": "10px",
                }
            ),  
        ], 
        className='div center_h'
        ),

        html.Div(children=[
            html.Div(children=[
                dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_means', className='dropdown',),
                dcc.Graph(id="graph_mult_lines", figure=plots.fig_moving_avg, className='graph_max_width')
                ],
                style={"flex": "1", "padding": "10px"}
            ),],
            style={"flex": "1", "padding": "10px"},
            className='div'
        )        
    ],
    )
])