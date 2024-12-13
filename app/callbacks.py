from dash import Input, Output, callback
from dash.exceptions import PreventUpdate
import app 
import data_manager
import plots

#Atualizar os dados ao clilcar no botao
@callback(
    Input('update_infos', 'n_clicks'),
    running=[(Output("update_infos", "disabled"), True, False)]
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        data_manager.att_info()

# region Mudar o calculo da KPIs
@callback(
    Output('kpis_durations', 'children'),
    Input('radio_options_kpis', 'value')
)
def change_kpis(value):
    return plots.kpis('durations', func=value)
@callback(
    Output('kpis_comments', 'children'),
    Input('radio_options_kpis', 'value')
)
def change_kpis(value):
    return plots.kpis('comments', func=value)
@callback(
    Output('kpis_likes', 'children'),
    Input('radio_options_kpis', 'value')
)
def change_kpis(value):
    return plots.kpis('likes', func=value)
@callback(
    Output('kpis_views', 'children'),
    Input('radio_options_kpis', 'value')
)
def change_kpis(value):
    return plots.kpis('views', func=value)
#endregion

#Mudar grafico de barra todos
@callback(
    Output('graph-bar-all', 'figure'),
    Input('radio-options-graph-bar-all', 'value')
)
def change_graph_bar(value):
    return plots.change_fig_bar_all(value)


#Mudar a view do grafico de linha
@callback(
    Output('graph_mult_lines', 'figure'),
    Input('radio-options-graph-mult-lines', 'value')
)
def change_view(value):
    fig_moving_avg = plots.change_fig_moving(value)
    return fig_moving_avg