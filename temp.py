from websocket import create_connection
from binance.client import Client
import time
import threading
api_key = '1GTn7SOVpDXUDWpj8cTOoPxFnrzr07LYK8ETsVj4GmuzQ6jysT3ZJIxJUHdqpX6f'
api_secret = 'ozU7KjW8D04JryMGEyA4ViEz6bpXGrOLGoErVBhM88YHUpptSbASs8rfobXYauYT'

from binance.client import Client

def yl():
    print('thead')
    
live_feed_thread = ''
live_feed_thread = threading.Thread(target=yl)
live_feed_thread.start()

# client = Client(api_key,api_secret)
# fcs = client.futures_coin_symbol_ticker()
# print(fcs)

# fcs = client.get_symbol_ticker()
# for i in fcs:
#     print(i)


# baseUrl = 'wss://dstream.binance.com/stream?streams'
# ws = create_connection('wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker')
# while True:
#     print('in')
#     data = ws.recv()
#     print(data)
#     time.sleep(1)

# a = "my string"
# a = a.replace(' ','')
# print(list(a))
# def handle_socket_message(msg):
#     # print(f"message type: {msg['e']}")
#     print(msg)

# symbol = 'BNBBTC'
# twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
# twm.start_k
# line_socket(callback=handle_socket_message, symbol=symbol)
# twm.start()