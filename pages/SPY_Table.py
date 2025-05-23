import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

columns = ['Date','Close','Volume']


spy = pd.read_csv('https://raw.githubusercontent.com/SarmenSinanian/DS-Unit-2-Applied-Modeling/master/SPY.csv',
                   usecols = columns)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='SPY ETF Performance'),
    generate_table(spy)
])