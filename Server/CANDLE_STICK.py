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


def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')# retrives data on a daily basis /or 
	web=yf.download(tikr,start,end)

	#Reset the index to remove Date column from index
	web_ohlc = web.reset_index()


	#Naming columns
	web_ohlc.columns = ["Date","Open","High",'Low',"Close","Adj Close","Volume"]

	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)

	'''
	pylab.rcParams['figure.figsize'] = (20, 9)
	ax1 = plt.subplot2grid((8,1), (0,0), rowspan=8, colspan=1)
	plt.tight_layout()

	ax1.xaxis_date()
	plt.xlabel("Date")
	print(web_ohlc)

	candlestick_ohlc(ax1,web_ohlc.values,width=1.5, colorup='g', colordown='r',alpha=0.75)
	plt.ylabel("Price")
	plt.legend(loc=2)# shows label in the left most postion of the graph 

	plt.show()
	'''
	
	table=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table.append([str(list(web_ohlc["Date"])[i]),str(list(web_ohlc["Open"])[i]),str(list(web_ohlc["High"])[i]),str(list(web_ohlc["Low"])[i]),str(list(web_ohlc["Close"])[i]),str(list(web_ohlc["Adj Close"])[i]),str(list(web_ohlc["Volume"])[i])])

	print(table)
	return table
