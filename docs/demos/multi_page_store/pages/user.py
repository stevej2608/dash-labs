from dash import html, Input, Output, callback, no_update as NO_UPDATE, callback_context
import dash

dash.register_page(__name__, path="/user")

layout = html.H1("Hello guest@gmail.com", id='user')

@callback(Output('user', 'children'), Input('store', 'data'))
def _login_cb(data):

    print('_login_cb')

    ctx = callback_context
    if not ctx.triggered:
        print('  NOT triggered')

    if data:
        print('  Valid store data available')
        return f"Hello {data['email']}"
    else:
        return NO_UPDATE