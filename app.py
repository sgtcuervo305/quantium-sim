# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



import csv
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from datetime import datetime

app = Dash()



with open('filtered_results.csv', 'r') as file:
    reader = pd.read_csv(file)
    data = [row for row in reader]

dates = [datetime.fromisoformat(row[1]).date() for row in data[1:]]
dates.pop(0)
   
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Time": [range(min(dates), max(dates) + 1)],
    "Amount Sold": [range(500,601)],
    "Region": ["North", "South", "East", "West"]
})

fig = px.line(df, x="Time", y="Amount Sold", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
