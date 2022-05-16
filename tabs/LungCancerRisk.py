from plotly.tools import mpl_to_plotly
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import pickle
import numpy as np
import pandas as pd
import shap
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import base64
from io import BytesIO

from app import app

style = {'padding': '1.5em'}

layout = html.Div([
  html.P([html.Br()]),
  html.P([html.Br()]),
  dcc.Markdown('#### Seven questions to predict the risk of lung cancer:'),
  dcc.Markdown('Each form must be carefully filled out to obtain the prediction'),
  html.P([html.Br()]),
  dcc.Markdown('###### What is your age?'),
  dcc.Input(
    id='age',
    placeholder='Enter a value',
    type='number',
    value=''),
  dcc.Markdown('###### Do you have a family history of lung cancer?'),
  dcc.Dropdown(
    id='lung_cancer_family_history',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),
  dcc.Markdown('###### What is your current smoking status?'),
  dcc.Dropdown(
    id='smoking_status',
    options=[
        {'label': 'Current cigarette smoker', 'value': '1'},
        {'label': 'Former cigarette smoker', 'value': '2'}
    ],
    value='',
  ),
  dcc.Markdown('###### At what age did you start smoking?'),
  dcc.Input(
    id='age_started_smoking',
    placeholder='Enter a value',
    type='number',
    value=''),
  dcc.Markdown("""###### How many years did you smoke?"""),
  dcc.Input(
    id='years_smoking',
    placeholder='Enter a value',
    type='number',
    value=''),
    dcc.Markdown("""###### How many packs of cigarettes do/did you smoke each day?"""),
  dcc.Input(
    id='packs',
    placeholder='Enter a value',
    type='number',
    value=''),
  dcc.Markdown('###### If you are not a current smoker, how many years passed since you stopped smoking? If you are still smoking, answer "0".'),
  dcc.Input(
    id='years_since_stopped_smoking',
    placeholder='Enter a value',
    type='number',
    value=''),
  html.P([html.Br()]),  
  html.P([html.Br()]),
  html.Div(html.P(['The predicted probability of lung cancer is:']), style={'fontWeight': 'bold', 'color': '#48a1af', 'font-size': 'large', 'text-align': 'center'}),
  html.Div(id='LungCancerRisk-content', style={'fontWeight': 'bold', 'color': '#48a1af', 'font-size': 'large', 'text-align': 'center'}),
  html.Div(html.P(['This chart shows the most important features associated with a higher (red) or lower (blue) risk of lung cancer']), style={'fontWeight': 'bold', 'color': '#48a1af', 'font-size': 'large', 'text-align': 'center'}),
  html.P([html.Br()])
])

@app.callback(
    Output('LungCancerRisk-content', 'children'),
    [Input('age', 'value'),
     Input('lung_cancer_family_history', 'value'),
     Input('smoking_status', 'value'),
     Input('age_started_smoking', 'value'),
     Input('years_smoking', 'value'),
     Input('packs', 'value'),
     Input('years_since_stopped_smoking', 'value')])

def predict(age,lung_cancer_family_history,smoking_status,age_started_smoking,years_smoking,packs,years_since_stopped_smoking):

  age = float(age)
  lung_cancer_family_history = float(lung_cancer_family_history)
  smoking_status = float(smoking_status)
  age_started_smoking = float(age_started_smoking)
  years_smoking = float(years_smoking)
  packs = float(packs)
  years_since_stopped_smoking = float(years_since_stopped_smoking)
  pack_years = packs * years_smoking

  df = pd.DataFrame(
    columns=['age','lung_cancer_family_history','smoking_status','age_started_smoking','pack_years','years_since_stopped_smoking'],
    data=[[age,lung_cancer_family_history,smoking_status,age_started_smoking,pack_years,years_since_stopped_smoking]]
    )

  model = pickle.load(open('models/LungCancerRisk.pkl', 'rb'))
  y_pred_proba = model.predict_proba(df)[:,1]
  y_pred = float(y_pred_proba) * 100
  y_pred = np.round(y_pred, 0)
  results = f'{y_pred}%'

  explainer = shap.TreeExplainer(model)
  shap_values = explainer.shap_values(df)
  shap.force_plot(explainer.expected_value, shap_values, df, matplotlib=True, show=False)
  buf = BytesIO()
  plt.savefig(buf, format="png")
  data = base64.b64encode(buf.getbuffer()).decode("ascii")
  displ = html.Div(html.P([html.Br(), html.Br(), html.Br()]))
  graph = html.Img(src='data:image/png;base64,{}'.format(data), style={'width' : '900px', 'text-align': 'center'})

  return results, displ, graph