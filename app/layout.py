from dash import html, dcc
import plots

layout = html.Div(children=[
    html.Div(children=[
        html.Header(children='Highlights da Temporada de Fórmula 1 - 2024', className='title'),
        html.Button('Atualizar', id='update_infos', className='btn'),
        ], className='div'),

    html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                dcc.Dropdown(['views', 'likes', 'comments'], value='views', id='list_engagement', clearable=False, className='dropdown',),
                dcc.Graph(id="graph_bars_top_engagement", figure=plots.fig_bar_top_engagement),
            ], style={"flex": "1", "padding": "10px"}),  

        dcc.Graph(id="graph_bars_periods", figure=plots.fig_bar_periods, 
                  style={"flex": "1", "padding": "10px"}),  
    ], className='div'),

        html.Div(children=[
            html.Div(children=[
                dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_means', className='dropdown',),
            dcc.Graph(id="graph_mult_lines", figure=plots.fig_moving_avg)
            ], style={"flex": "1", "padding": "10px"}),
            html.Div(children=[
                html.H2(children="KPI's", className=' title subtitle'),
                html.Div(children=[
                    html.Div(children=[
                        html.H3(children="vizualizações", className=' title subtitle minsubtitle'),
                        html.P(children=plots.kpis('views'))
                    ], className='center'),
                    html.Div(children=[
                        html.H3(children="curtidas", className=' title subtitle minsubtitle'),
                        html.P(children=plots.kpis('likes'))
                    ], className='center'),
                    html.Div(children=[
                        html.H3(children="comentarios", className=' title subtitle minsubtitle'),
                        html.P(children=plots.kpis('comments'))
                    ], className='center'),
                    html.Div(children=[
                        html.H3(children="Duração", className=' title subtitle minsubtitle'),
                        html.P(children=plots.kpis('durations'))
                    ], className='center'),
                ], className='div midrow')
            ], className='grid-container grid_max_width')

        ],style={"flex": "1", "padding": "10px"},className='div')
        
    ])
])