
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt 
import matplotlib
import pylab
import matplotlib.dates as mdates

def main(tikr):
	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)

	web_ohlc = web.reset_index()

	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)

	table=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table.append([str(list(web["Open"])[i]),str(list(web["High"])[i]),str(list(web["Low"])[i]),str(list(web["Close"])[i]),str(list(web["Adj Close"])[i]),str(list(web["Volume"])[i]),str(list(web_ohlc["Date"])[i])])
	print(table)
	return table
