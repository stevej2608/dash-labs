from dash import dcc
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc

store = dcc.Store('store', storage_type='session')

app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container(
    [store, dl.plugins.page_container],
    fluid=True,
)

# usage:
#   python -m docs.demos.multi_page_store.app

if __name__ == "__main__":
    print('Starting...')
    app.run_server(debug=False, threaded=False)
