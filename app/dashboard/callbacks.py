from dash.dependencies import Input, Output
from plotly.graph_objs._figure import Figure
from market_data import market_data
import dash_table

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go


def load_callbacks(app):
    @app.callback(Output('aggregate_data', 'data'),
                  [Input('dropdown', 'value')])
    def update_ticker(value):
        if value:
            df = market_data(value).df
            df['Date'] = df.index.date

            data = {}
            data['columns'] = df.columns
            data['records'] = df.to_dict('records')
            data['graph_x'] = df['Date']
            data['graph_y'] = df['Close']
            return data

    @app.callback(Output('row2', 'children'),
                  [Input('aggregate_data', 'data'),Input('dropdown', 'value')])
    def update_table(data,value):
        if data:

            fig = go.Figure(data=[go.Scatter(x=data['graph_x'], y=data['graph_y'])])
            fig.update_layout(
                title=f"Closing Price of {value}",
                xaxis_title="Date",
                yaxis_title="Closing",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(50,50,50,0)',
                margin=dict(
                    l=0,
                    r=0,
                    b=0,
                ),
        )    

            return html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(
                                id='graph',
                                figure = fig
                            )
                        ],
                        id="table_Container",
                        className="pretty_container"

                    ),
                ],
                className="twelve columns"

            )

    @app.callback(Output('row3', 'children'),
                  [Input('aggregate_data', 'data')])
    def update_graph(data):
        if data:
            return html.Div(
                [
                    html.Div(

                        [
                            dash_table.DataTable(
                                id='table',
                                columns=[
                                    {"name": 'Date', "id": 'Date'},
                                    {"name": 'Open', "id": 'Open'},
                                    {"name": 'High', "id": 'High'},
                                    {"name": 'Low', "id": 'Low'},
                                    {"name": 'Close', "id": 'Close'},
                                    {"name": 'Volume', "id": 'Volume'},
                                ],
                                fixed_rows={'headers': True},
                                data=data['records'],
                                style_table={

                                    'max-height': '200px'
                                }
                            )
                        ],
                        id="table_Container",
                        className="pretty_container"

                    ),
                ],
                className="twelve columns"

            )
