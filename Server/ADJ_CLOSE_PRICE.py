import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import pylab

def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)
	
	#Reset the index to remove Date column from index
	web_ohlc = web.reset_index()
	
	#Naming columns
	web_ohlc.columns = ["Date","Open","High",'Low',"Close","Adj Close","Volume"]
	
	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)

	'''
	pylab.rcParams['figure.figsize'] = (20, 9)
	print(web["Adj Close"])
	plt.plot(web_ohlc["Date"],web["Adj Close"])
	plt.show()
	'''
	table=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table.append([str(list(web_ohlc["Date"])[i]),str(list(web["Adj Close"])[i])])
		
	print(table)
	
	return table

