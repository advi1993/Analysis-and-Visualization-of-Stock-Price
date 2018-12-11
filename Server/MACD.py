
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib
import pylab
import matplotlib.dates as mdates
import datetime as dt

def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)
	web_close=pd.DataFrame(web.Close)
	#display(web_close)
	web['26 ema'] = web_close.ewm(com=26).mean()
	web['12 ema'] = web_close.ewm(com=12).mean()

	web_ohlc = web.reset_index()
	
	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)
	
	#print (web['26 ema'],web['12 ema'])
	web['MACD'] = (web['12 ema'] - web['26 ema'])
	print(web['MACD'])
	
	pylab.rcParams['figure.figsize'] = (20, 9)

	plt.plot(web['MACD'],label='MACD')
	plt.legend(loc=2)
	plt.savefig('./plot.png')
	plt.close()
	#plt.show()
	
	table=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table.append([str(list(web_ohlc["Date"])[i]),str(web['MACD'][i])])
	
	print(table)
	return table

