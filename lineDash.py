import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the sales data
df = pd.read_csv('formatted_data.csv')

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort data by date
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Sales Data Visualizer'),

    dcc.Graph(
        id='sales-line-chart',
    )
])

# Add callback to update graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('sales-line-chart', 'id')
)
def update_graph(input_value):
    fig = px.line(df, x='date', y='sales', title='Sales Over Time')
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
