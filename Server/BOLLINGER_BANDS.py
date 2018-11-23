
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib
import pylab
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)
	web_close=pd.DataFrame(web.Close)  # assigning close prices to web_ close 

	web_close["MA_20"]=web_close.Close.rolling(20).mean() # moving average of close prices of 20 days 
	
	web_ohlc = web.reset_index()
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)
	dates = list(web_ohlc['Date'])

	web["20 Day STD"] = web.Close.rolling(20).std()
	web["Upper Band"] = web_close["MA_20"] + (web['20 Day STD'] * 2) # adding 20 day moving average to 20 day standard deviation 
	web["Lower Band"] = web_close["MA_20"] - (web['20 Day STD'] * 2) # for lower band subtracting 20 day moving average and 20 day standard deviation 
	pylab.rcParams['figure.figsize'] = (20, 9)
	'''
	plt.plot(web_close["Close"],label='Close')
	plt.plot(web_close["MA_20"],label="MA 20 days")
	plt.plot(web["Upper Band"], label="Upperband")
	plt.plot(web["Lower Band"], label="Lowerband")
	plt.legend(loc=2)
	plt.show()
	'''
	table=[]
	for  i in range(len(list(web_close["Close"]))):
		table.append([str(list(web_close["Close"])[i]),str(list(web_close["MA_20"])[i]),str(list(web["Upper Band"])[i]),str(list(web["Lower Band"])[i]),str(dates[i])])

	print(table)
	print(len(list(web_close["Close"])))
	print(len(list(web_close["MA_20"])))
	print(len(list(web["Upper Band"])))
	print(len(list(web["Lower Band"])))
	return(table)
