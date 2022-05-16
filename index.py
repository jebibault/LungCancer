from dash.dependencies import Input, Output
from dash import dcc
from dash import html

from app import app, server
from tabs import intro, disclaimer, LungCancerRisk, LungCancerDeath

style = {
    'maxWidth': '70%', 
    'margin': 'auto'}

app.title = 'Lung cancer risk prediction with AI'

app.layout = html.Div([
    html.P([html.Img(src='assets/logo.png', style={'width' : '100%', 'margin-bottom': '0px', 'margin-top': '20px'})]),
    html.P([
	    html.Br()]),
    dcc.Tabs(id='tabs', value='tab-intro', parent_className='custom-tabs', className='custom-tabs-container', children=[
        dcc.Tab(label='About', value='tab-intro', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Lung Cancer Risk', value='tab-LungCancerRisk', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Lung Cancer Death', value='tab-LungCancerDeath', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Disclaimer', value='tab-disclaimer', className='custom-tab', selected_className='custom-tab--selected'),
    ]),
    html.Div(id='tabs-content-classes'),
], style=style)

@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-LungCancerRisk': return LungCancerRisk.layout
    elif tab == 'tab-disclaimer': return disclaimer.layout
    elif tab == 'tab-LungCancerDeath': return LungCancerDeath.layout

if __name__ == '__main__':
    app.run_server(debug=True)
