from dash import Input, Output, callback
from dash.exceptions import PreventUpdate
import app 
import data_manager
import plots

#atualizar os dados ao clilcar no botao
@callback(
    Input('update_infos', 'n_clicks'),
    running=[(Output("update_infos", "disabled"), True, False)]
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        data_manager.att_info()

#mudar a view do grafico de linha
@callback(
    Output('graph_mult_lines', 'figure'),
    Input('list_means', 'value')
)
def change_view(value):
    df = data_manager.get_playlistInfo()
    value = value +'_moving_avg'
    plots.fig_moving_avg.data[-1].y = df[value]
    return plots.fig_moving_avg
#mudar a view do grafico de barras
@callback(
    Output('graph_bars_top_engagement', 'figure'),
    Input('list_engagement', 'value')
)
def change_view(value):
    fig_bar_top_engagement = plots.change_fig_bar(value)
    return plots.fig_bar_top_engagement