# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



import csv
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from datetime import datetime

app = Dash()



with open('filtered_results.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

dates = [datetime.fromisoformat(row[1]).date() for row in data[1:]]
x = [row[2] for row in data[1:]]  #region
y = sorted([row[0] for row in data[1:]])  #amount sold

   
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Time": dates,
    "Amount Sold": y,
    "Region": x
})
print(df)
fig = px.line(df, x="Time", y="Amount Sold", color='Region')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales'),

    html.Div(children='''
        Graph showing sales of Pink Morsels over time by region.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
