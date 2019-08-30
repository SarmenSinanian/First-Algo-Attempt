import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
from joblib import load
from app import app

from app import app

# pipeline = load('assets/pipeline.joblib')

# columns = ['Date','Close','Volume']
# spy['Date_String'] = spy['Date']
# spy['Date'] = pd.to_datetime(spy['Date'])

# Calling data set (from github)
# spy = pd.read_csv('https://raw.githubusercontent.com/SarmenSinanian/DS-Unit-2-Applied-Modeling/master/SPY.csv', usecols = columns)

# print('Model loaded successfully')

# def predict(RSI_Yesterday_EXP):
#     # df = pd.DataFrame(
#     #     data=[[RSI_Yesterday_EXP]],
#     #     columns=['RSI_Yesterday_EXP']
#     # )
#     df = spy[spy['Date'] == '2019-05-14']
#     # df = spy['RSI_Yesterday_EXP']
#     pred = pipeline.predict(df)[0]
    
#     # explainer = shap.TreeExplainer(model)
#     # shap_values = explainer.shap_values(df)
    
# #     feature_names = df.columns
# #     feature_values = df.values[0]
# #     shaps = pd.Series(shap_values[0], zip(feature_names, feature_values))
    
#     result = [html.Div(f'Percent chance of closing higher {pred:,.0f} \n\n')]
# #     result.append(html.Div(f'Starting from a baseline of ${explainer.expected_value:,.0f}. \n'))
# #     explanation = shaps.to_string()
# #     lines = explanation.split('\n')
# #     for line in lines:
# #         result.append(html.Div(line))
#     return result

# # example = 

# # result = predict(23.557179)

# result = predict(date = '2016-01-04')

# mask = (spy['Date'] == '2016-01-04')

# spyy = spy.loc[mask]
 
# df = spy.loc[mask]
# df


column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Year'), 
        dcc.Slider(
            id='year', 
            min=1955, 
            max=2055, 
            step=5, 
            value=2020, 
            marks={n: str(n) for n in range(1960,2060,20)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Continent'), 
        dcc.Dropdown(
            id='continent', 
            options = [
                {'label': 'Africa', 'value': 'Africa'}, 
                {'label': 'Americas', 'value': 'Americas'}, 
                {'label': 'Asia', 'value': 'Asia'}, 
                {'label': 'Europe', 'value': 'Europe'}, 
                {'label': 'Oceania', 'value': 'Oceania'}, 
            ], 
            value = 'Africa', 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Based on the previous day\'s data, our model would have guessed we are going to close', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])