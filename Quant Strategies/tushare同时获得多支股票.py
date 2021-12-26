import tushare as ts
import pandas as pd
#编写函数同时获得多只股票的数据
def multiple_stocks(tickers):
	def data(ticker):
		stocks = ts.get_k_data(ticker,start='2016-01-01',end = '2017-07-01')
		stocks.set_index('date',inplace = True)
		stocks.index = pd.to_datetime(stocks.index)
		return stocks

	datas = map(data, tickers)

	return pd.concat(datas, keys=tickers, names=['Ticker','Date'])

tickers = ['600030', '000001', '600426']
all_stocks = multiple_stocks(tickers)
print(all_stocks.tail())