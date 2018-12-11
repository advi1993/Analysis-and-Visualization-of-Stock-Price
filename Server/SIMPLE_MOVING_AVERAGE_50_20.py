
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import pylab

def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download("MSFT",start,end)

	web_close=pd.DataFrame(web.Close)
	web_close["MA_20"]=web_close.Close.rolling(20).mean()
	web_close["MA_50"]=web_close.Close.rolling(50).mean()

	#Reset the index to remove Date column from index
	web_ohlc = web.reset_index()

	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)

	pylab.rcParams['figure.figsize'] = (20, 9)
	plt.grid(True)
	plt.plot(web_close['Close'],label='Close')
	plt.plot(web_close["MA_20"],label="MA 20 days")
	plt.plot(web_close["MA_50"],label="MA 50 days")
	plt.legend(loc=2)
	plt.savefig('./plot.png')
	plt.close()
	#plt.show()
	
	table=[]
	for  i in range(len(list(web_close["Close"]))):
		table.append([str(list(web_close["Close"])[i]),str(list(web_close["MA_20"])[i]),str(list(web_close["MA_50"])[i]),str(list(web_ohlc["Date"])[i])])
	
	print(table)
	return table
