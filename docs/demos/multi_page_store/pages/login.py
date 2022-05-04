import dash

dash.register_page(__name__, path="/login")

from dash import dcc, html, Input, Output, State, callback, no_update as NO_UPDATE

email = dcc.Input(id='email', name='email', type='email', placeholder="Enter email")
button = html.Button('Sign In', type='submit', id='btn')
redirect = dcc.Location(id='redirect', refresh=True)

layout = html.Div([email, button, redirect])

@callback(Output('redirect', 'href'), Output('store', 'data'), State('email', 'value'), Input('btn', 'n_clicks'))
def email_cb(email, clicks):
    _redirect = NO_UPDATE
    _store = NO_UPDATE
    if clicks:
        _redirect = '/user'
        _store = {'email' : email}

    return _redirect, _store

