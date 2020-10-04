import dash_html_components as html
import dash_core_components as dcc


def load_layout(app,tickers):
    app.layout = html.Div([
        dcc.Store(
            id='aggregate_data'),
        html.Div(  # header
            [
            html.Div(
                html.H6('Stock Data of S&P 500'),
                className='eight columns'
            ),

            html.Div(

                className='two columns'
            ),

            
            html.A([
                html.Img(
                    src="https://github.githubassets.com/images/modules/logos_page/Octocat.png",
                    style={'height':'100%', 'width':'50%','float': 'right'},                    
            ),
            ],
            href = "https://github.com/quazirab/stock_data_s-p_500",
            className='two columns',
            ),
            
            ],
            id="header",
            className='row',
        ),

        html.Div(
            [   
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.Dropdown(
                                    options=tickers,
                                    id='dropdown',
                                )
                            ],
                            id="dropdown_Container",
                            className="pretty_container"
                        ),
                    ],
                    className="twelve columns"

                ),

            ],
            id="row1",
            className="row"
        ),

        
        html.Div(
            id="row2",
            className="row"
        ),

        html.Div(
            id="row3",
            className="row"
        ),


        

    ],
        id="mainContainer",
        style={
        "display": "flex",
        "flex-direction": "column"
    }
    )
