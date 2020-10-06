from yfinance import Ticker

class market_data(Ticker):
    def __init__(self,ticker,period="6mo"):
        super(market_data,self).__init__(ticker)
        self.__period = period
        self._init_df()
    
    @property
    def period(self):
        return self.__period
    @period.setter
    def period(self,p):
        self.__period = p
        self._init_df()

    @property
    def df_dashboard(self):
        return self.__df

    @property
    def columns(self):
        return self.__df.columns
    
    @property
    def close(self):
        return self.__df['Close']

    @property
    def volume(self):
        return self.__df['Volume']

    @property
    def dict_dashboard(self):
        df = self.__df
        df['Date'] = df.index
        return df.to_dict('records')

    @property
    def date(self):
        return self.__df.index

    @property
    def dict_api(self):
        df = self.__df
        df.index = df.index.astype(str)
        return df.to_dict('index')

    def _init_df(self):
        self.__df=super(market_data,self).history(period=self.__period)
        self.__df.index = self.__df.index.date
    
    
    


    