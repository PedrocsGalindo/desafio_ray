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
    Output('grafico-multiplas-linhas', 'figure'),
    Input('lista_medias', 'value')
)
def change_view(value):
    df = data_manager.get_playlistInfo()
    value = value +'_moving_avg'
    plots.fig_moving_avg.data[-1].y = df[value]
    return plots.fig_moving_avg