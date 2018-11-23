
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like # Used as a patch for pandas data reader to avoid error
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt
import numpy as np
import matplotlib
import pylab
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import matplotlib.font_manager as font_manager
from IPython import get_ipython
import tkinter

#get_ipython().run_line_magic('matplotlib','inline')
#get_ipython().run_line_magic('pylib','inline')

#%matplotlib inline
#%pylab inline

def rsiFunc(prices, n=14):
    deltas = np.diff(prices,axis=0)
    
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n     #moving average of last 14 days prices
    down = -seed[seed<0].sum()/n
    rs = (up/down)
    rsi= np.zeros_like(prices)
    rsi[:n] = 100. - (100./(1.+rs))

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = abs(up/down)
        rsi[i] = 100. -(100./(1.+rs))
    return rsi
    
    
def main(tikr):    
	
	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)
	
	web_close=pd.DataFrame(web.Close)
	  
	#print (len(web_close))
	#matplotlib.rcParams.update({'font.size': 9})


	#Reset the index to remove Date column from index
	web_ohlc = web.reset_index()

	#Naming columns
	web_ohlc.columns = ["Date","Open","High",'Low',"Close","Adj Close","Volume"]

	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)

	dates = list(web_ohlc['Date'])

	prices=web_close
	rsi=rsiFunc(prices)
	#print (rsi)# PRINTING THR RSI VALUES 

	#plotting RSI INDICATOR
	
	'''
	pylab.rcParams['figure.figsize'] = (20, 9)#this function makes the graph bigger and presentable 
	ax= plt.gca()
	ax.xaxis_date()
	plt.xlabel("Date")
	plt.plot(web_ohlc['Date'],rsi)
	plt.ylim(0,100)
	plt.yticks([30, 70])
	plt.show()
	'''
	
	table=[]
	for  i in range(len(rsi)):
		table.append([rsi[i][0],str(dates[i])])

	print(table)
	return table
