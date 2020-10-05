
## [S&P 500 Stock Market Web App](https://stock-500.herokuapp.com/)

The web-application visualizes S&P 500 stock market data. 

The application is written in Python and uses Flask, Dash yFinance and Pandas. It is staged and deployed using Heroku pipeline. 

The app doesnot use any database. It collects data from yFinance (Yahoo Finance API) and creates an `market_data` object, which then gets used in the `app.dashboard.callbacks` function for generating graph and table. 

### Snapshot
![snapshot1](snapshot/snap1.gif?raw=true "Snapshot 1")

### Pipeline
![pipeline](snapshot/pipeline.png?raw=true "Heroku Pipeline")

### Installation
1. Create virtualenv `venv` for python-3.7
1. Activate virtualenv
1. Install requirements ```pip install -r requirements.txt```
1. run server ```gunicorn run_server:server```


