import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib
import pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime as dt
import matplotlib
import pylab

def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)

	web_ohlc = web.reset_index()

	#Naming columns
	web_ohlc.columns = ["Date","Open","High",'Low',"Close","Adj Close","Volume"]

	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)
	
	pylab.rcParams['figure.figsize'] = (20, 9)
	ax= plt.gca() #used to set "get current axes".Current here means that it provides a handle to the last active axes. If there is no axes yet, an axes will be created. If you create two subplots, the subplot that is created last is the current one.
	ax.xaxis_date()

	plt.plot(web_ohlc['Date'],web_ohlc.Close)
	plt.plot(web_ohlc['Date'],web_ohlc.Open)
	plt.plot(web_ohlc['Date'],web_ohlc.High)
	plt.plot(web_ohlc['Date'],web_ohlc.Low)
	
	plt.ylabel("Price")
	plt.xlabel("Dates")
	plt.legend(loc=2)
	plt.savefig('./plot.png')
	plt.close()
	#plt.show()
	
	
	table=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table.append([str(list(web_ohlc["Date"])[i]),str(list(web_ohlc["Open"])[i]),str(list(web_ohlc["High"])[i]),str(list(web_ohlc["Low"])[i]),str(list(web_ohlc["Close"])[i]),str(list(web_ohlc["Adj Close"])[i]),str(list(web_ohlc["Volume"])[i])])
	
	print(table)
	return table
