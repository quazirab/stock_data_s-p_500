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
    def df(self):
        return self.__df

    def _init_df(self):
        self.__df=super(market_data,self).history(period=self.__period)
    
    @property
    def close(self):
        return self.__df['Close']
    
    @property
    def volume(self):
        return self.__df['Volume']

    