import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import DOWNLOAD_DATA
import RSI
import BOLLINGER_BANDS
import CANDLE_STICK
import ADJ_CLOSE_PRICE
import CCI
import MACD
import OHLC_LINE_PLOT
import SIMPLE_MOVING_AVERAGE_50_20
import base64

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print('new connection')
		 
	def on_message(self, message):
		mode = int((message.split(','))[1])
		tikr = (message.split(','))[0]
		
		print(mode)
		
		print('message received:  %s' % message)
		# Reverse Message and send it back
		# print('sending back message: %s' % message[::-1])
		if mode == 1:
			RSI.main(tikr)
		if mode == 2:
			CCI.main(tikr)
		if mode == 3:
			MACD.main(tikr)
		if mode == 4:
			BOLLINGER_BANDS.main(tikr)
		if mode == 5:
			SIMPLE_MOVING_AVERAGE_50_20.main(tikr)
		if mode == 6:
			CANDLE_STICK.main(tikr)
		if mode == 7:
			OHLC_LINE_PLOT.main(tikr)
		if mode == 8:
			ADJ_CLOSE_PRICE.main(tikr)
		if mode == 9:
			DOWNLOAD_DATA.main(tikr)
		with open("plot.png","rb") as image_file:
			img = base64.b64encode(image_file.read())
		self.write_message(img)
			
	def on_close(self):
		print('connection closed')
 
	def check_origin(self, origin):
		return True
 
application = tornado.web.Application([
	(r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8888)
	myIP = socket.gethostbyname(socket.gethostname())
	print('*** Websocket Server Started at %s***' % myIP)
	tornado.ioloop.IOLoop.instance().start()
