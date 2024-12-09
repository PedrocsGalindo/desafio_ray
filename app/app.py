from dash import Dash
from layout import layout

app = Dash(__name__)

app.title = 'Highlights da Temporada de Fórmula 1 - 2024'
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)