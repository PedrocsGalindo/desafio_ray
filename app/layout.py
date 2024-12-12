from dash import html, dcc
import plots

layout = html.Div(children=[
    html.Div(children=[
        html.Header(children='Highlights da Temporada de Fórmula 1 - 2024', className='title title_border_bottom'),
        html.Button('Atualizar', id='update_infos', className='btn'),
        ], 
        className='grid_flex_row'
        
    ),
    html.Div(children=[
        html.Div(children=[
            html.Div(),
            html.Div(children=[
                dcc.RadioItems(id='radio_options_kpis', options=[
                    {"label": "Media", "value": "mean"},
                    {"label": "Maior", "value": "max"},
                    {"label": "Menor", "value": "min"},
                    {"label": "Soma", "value": "sum"}
                ], 
                value="mean", 
                labelStyle={"display": "flex", "alignItems": "center", "fontSize": "1.1em"},
                className="radio-container"
                ),
            ],
            className='grid_flex_row'
            ),
            html.Div(children=[
                html.H3(children="vizualizações", className=' title kpis_titles'),
                html.P(children=plots.kpis('views'), id='kpis_views', className='kpis_text_valeus')
            ], className='grid-pane div_kpis horizontal_center'
            ),
            html.Div(children=[
                html.H3(children="curtidas", className=' title kpis_titles'),
                html.P(children=plots.kpis('likes'), id='kpis_likes', className='kpis_text_valeus')
            ], className='grid-pane div_kpis horizontal_center'
            ),
            html.Div(children=[
                html.H3(children="comentarios", className=' title kpis_titles'),
                html.P(children=plots.kpis('comments'), id='kpis_comments', className='kpis_text_valeus')
            ], className='grid-pane div_kpis horizontal_center'
            ),
            html.Div(children=[
                html.H3(children="Duração", className=' title kpis_titles'),
                html.P(children=plots.kpis('durations'), id='kpis_durations', className='kpis_text_valeus')
            ], className='grid-pane div_kpis horizontal_center'
            )
        ],
        className='grid-pane column_6'
        ),
        html.Div(children=[
            dcc.Graph(id="graph_bars_periods", figure=plots.fig_bar_periods, 
                style={
                    "flex": "1", 
                }
            ),
            dcc.Graph(id='graph_pizza', figure=plots.fig_pizza),
        ],
        className='grid-pane column_fifty_fifty'
        ),
        html.Div(children=[
            html.Div(children=[
                dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_means', className='dropdown',),
                dcc.Graph(id="graph_mult_lines", figure=plots.fig_moving_avg, )
            ],
            style={"flex": "1", "padding": "10px"}
            ),
            html.H1(children='engajamento e relevancia aqui')
        ],
        className='grid-pane colunm_2'
        )
    ],
    className='grid-pane row_3'
    ),
],
className='conteiner'
)