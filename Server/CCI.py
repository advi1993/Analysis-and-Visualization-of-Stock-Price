
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import matplotlib
import pylab
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates

def main(tikr):

	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)
	web_close=pd.DataFrame(web.Close)
	web_high=pd.DataFrame(web.High)
	web_low=pd.DataFrame(web.Low)
	web_close["MA_20"]=web.Close.rolling(20).mean()
	web["20 Day STD"] = web.Close.rolling(20).std()
	
	#Reset the index to remove Date column from index
	web_ohlc = web.reset_index()
	
	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)
	
	TP=(web.High+web.Low+web.Close)/3
	CCI = pd.Series((TP -web_close["MA_20"]) / (0.015*web["20 Day STD"])) 
	'''
	pylab.rcParams['figure.figsize'] = (20, 9)
	plt.plot(CCI,label='CCI')
	plt.legend(loc=2)
	plt.show()
	'''
	table=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table.append([str(list(web_ohlc["Date"])[i]),str(CCI[i])])
	
	print(table)
	return table
