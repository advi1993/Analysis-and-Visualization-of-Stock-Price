
import pandas as pd
pd.core.common.is_list_like=pd.api.types.is_list_like
from pandas_datareader import data as web
import fix_yahoo_finance as yf
import datetime as dt 
import matplotlib
import pylab
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image
from pandas.tools.plotting import table

def main(tikr):
	start=dt.datetime(2017,9,1)
	end=dt.datetime.today().strftime('%Y-%m-%d')
	web=yf.download(tikr,start,end)

	web_ohlc = web.reset_index()

	#Converting dates column to float values
	web_ohlc['Date'] = web_ohlc['Date'].map(mdates.date2num)

	table2=[]
	for  i in range(len(list(web_ohlc["Date"]))):
		table2.append([str(list(web["Open"])[i]),str(list(web["High"])[i]),str(list(web["Low"])[i]),str(list(web["Close"])[i]),str(list(web["Adj Close"])[i]),str(list(web["Volume"])[i]),str(list(web_ohlc["Date"])[i])])
	print(table2)
	'''
	new_img = Image.new("L", (1600, 600), "white")
	new_img.putdata(table)
	new_img.save('plot.png')
	'''
	
	ax = plt.subplot(111, frame_on=False) # no visible frame
	ax.xaxis.set_visible(False)  # hide the x axis
	ax.yaxis.set_visible(False)  # hide the y axis

	table(ax, web)  # where df is your data frame

	plt.savefig('plot.png')
	plt.close()
	
	return table
