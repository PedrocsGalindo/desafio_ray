from dash import html, dcc
import plots

layout = html.Div(children=[
    html.Div(children=[
        html.Header(children='Highlights da Temporada de Fórmula 1 - 2024', className='title title_border_bottom'),
        html.Button('Atualizar', id='update_infos', className='btn'),
        ], 
        className='grid_flex grid_flex_row height-8vh'
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
                labelStyle={
                    "display": "flex",
                    "alignItems": "center", 
                    "gap": "10px",          
                    "fontSize": "1.1em"
                },
                className="radio-container"
                ),
            ],
            className='grid_flex grid_flex_row height-8vh'
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
            html.Div(children=[
                dcc.Graph(id='graph-bar-all', figure=plots.fig_bar_all),
                html.H1(children='carro'),
            ],
            className='grid_flex grid_flex_row')
        ],
        className='grid-pane column_fifty_fifty'
        ),
        html.Div(children=[
            html.Div(children=[
                dcc.Dropdown(['views', 'likes', 'comments'], value = 'views', id='list_means', className='dropdown'),
                dcc.Graph(id="graph_mult_lines", figure=plots.fig_moving_avg, )
            ],
            style={"flex": "1", "padding": "10px"}
            ),
        ],
        className='grid-pane'
        ),
        html.Div(children=[
            html.Div(children=[
                html.Div(
                    className="relevance-list-container",
                    children=[
                        html.H5("Top engagement", className="relevance-list-title"),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('1- ' + plots.df_tops_engagement['places'].iloc[0], className="currency-code"),
                                                html.H6(plots.df_tops_engagement['titles'].iloc[0], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_engagement['views'].iloc[0], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_engagement['likes'].iloc[0], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_engagement['comments'].iloc[0], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('2- ' + plots.df_tops_engagement['places'].iloc[1], className="currency-code"),
                                                html.H6(plots.df_tops_engagement['titles'].iloc[1], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_engagement['views'].iloc[1], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_engagement['likes'].iloc[1], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_engagement['comments'].iloc[1], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('3- ' + plots.df_tops_engagement['places'].iloc[2], className="currency-code"),
                                                html.H6(plots.df_tops_engagement['titles'].iloc[2], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_engagement['views'].iloc[2], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_engagement['likes'].iloc[2], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_engagement['comments'].iloc[2], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('4- ' + plots.df_tops_engagement['places'].iloc[3], className="currency-code"),
                                                html.H6(plots.df_tops_engagement['titles'].iloc[3], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_engagement['views'].iloc[3], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_engagement['likes'].iloc[3], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_engagement['comments'].iloc[3], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('5- ' + plots.df_tops_engagement['places'].iloc[4], className="currency-code"),
                                                html.H6(plots.df_tops_engagement['titles'].iloc[4], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_engagement['views'].iloc[4], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_engagement['likes'].iloc[4], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_engagement['comments'].iloc[4], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                )
            ], id='lista-engagement'
            ),
            html.Div(children=[
                html.Div(
                    className="relevance-list-container",
                    children=[
                        html.H5("Top relevance", className="relevance-list-title"),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('1- ' + plots.df_tops_relevance['places'].iloc[0], className="currency-code"),
                                                html.H6(plots.df_tops_relevance['titles'].iloc[0], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_relevance['views'].iloc[0], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_relevance['likes'].iloc[0], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_relevance['comments'].iloc[0], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('2- ' + plots.df_tops_relevance['places'].iloc[1], className="currency-code"),
                                                html.H6(plots.df_tops_relevance['titles'].iloc[1], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_relevance['views'].iloc[1], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_relevance['likes'].iloc[1], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_relevance['comments'].iloc[1], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('3- ' + plots.df_tops_relevance['places'].iloc[2], className="currency-code"),
                                                html.H6(plots.df_tops_relevance['titles'].iloc[2], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_relevance['views'].iloc[2], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_relevance['likes'].iloc[2], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_relevance['comments'].iloc[2], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('4- ' + plots.df_tops_relevance['places'].iloc[3], className="currency-code"),
                                                html.H6(plots.df_tops_relevance['titles'].iloc[3], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_relevance['views'].iloc[3], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_relevance['likes'].iloc[3], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_relevance['comments'].iloc[3], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="relevance-list-item",
                            children=[
                                html.Div(
                                    className="relevance-list-item-info",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.P('5- ' + plots.df_tops_relevance['places'].iloc[4], className="currency-code"),
                                                html.H6(plots.df_tops_relevance['titles'].iloc[4], className="currency-description"),
                                            ]
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-view-info",
                                    children=[
                                        html.Small("View", className="label-small"),
                                        html.H6(plots.df_tops_relevance['views'].iloc[4], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-like-info",
                                    children=[
                                        html.Small("Like", className="label-small"),
                                        html.H6(plots.df_tops_relevance['likes'].iloc[4], className="value-large"),
                                    ],
                                ),
                                html.Div(
                                    className="relevance-list-comments-info",
                                    children=[
                                        html.Small("Comments", className="label-small"),
                                        html.H6(plots.df_tops_relevance['comments'].iloc[4], className="value-large"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                )
            ], id='lista-relevancia'
            ),
        ],
        className='grid-pane column_fifty_fifty'
        ),
    ],
    className='grid-pane row_4'
    ),
],
className='conteiner'
)
