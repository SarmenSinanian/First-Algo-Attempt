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

pipeline = load('assets/pipeline.joblib')


print('Model loaded successfully')


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

# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             ## SPY Chart


#             """
#         ),
#     ],
#     md=4,
# )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     )
# ])


columns = ['Date','Close','Volume']

spy = pd.read_csv('https://raw.githubusercontent.com/SarmenSinanian/DS-Unit-2-Applied-Modeling/master/SPY.csv', usecols = columns)
spy['Date'] = pd.to_datetime(spy['Date'])
matplotlib_figure = plt.figure()


# plt.scatter(spy['Date'], spy['Close'])
# plotly_figure = mpl_to_plotly(matplotlib_figure)


# if __name__ == '__main__':
#     app.run_server(debug=True)

column2 = dbc.Col(
    [
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': spy['Date'], 'y': spy['Close'], 'type': 'scatter'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

# column3 = dbc.Col(
#     [
#         dcc.Graph(figure=matplotlib_figure)
#     ]
# )
    
# # columns = ['Date','Close','Volume']

# # spy = pd.read_csv('https://raw.githubusercontent.com/SarmenSinanian/DS-Unit-2-Applied-Modeling/master/SPY.csv',
# #                    usecols = columns)

# # def generate_table(dataframe, max_rows=10):
# #     return html.Table(
# #         # Header

layout = dbc.Row([column1, column2])