import time
import pandas
from websocket import create_connection
print(pandas.__file__)

from binance.client import Client

class Bnb_Trade:
    socket_list = ['']
    socket = 'close'
    def trade(self,binance_key,binance_secret):
        self.symbol_list = []
        self.binance_key = binance_key
        self.binance_secret = binance_secret
        self.client = Client(self.binance_key,self.binance_secret)
        fcs = self.client.get_symbol_ticker()
        for i in fcs:
            self.symbol_list.append(i['symbol'])
        return self.symbol_list

    # def socket_manager(self,symbol):
    #     print(symbol)
    #     if symbol not in self.socket_list:
    #         if self.socket == 'open':
    #             time.sleep(1000)
    #             print("Socket being closed")
    #             # self.bm.stop_socket(self.conn_key)
    #             # self.bm.close()
    #         self.socket_list.clear()
    #         self.socket_list.append(symbol)
    #         # self.bm = BinanceSocketManager(self.client)
    #         # self.conn_key = self.bm.start_symbol_ticker_deliver_socket(str(symbol),self.process_message)
    #         # self.bm.start()
    #         self.socket == 'open'
    #         print('self.socket OPEN========================')
    #     else:
    #         pass

    def socket_connect(self,symbol_str=None):
        if symbol_str!=None:
            if self.socket == 'open':
                baseUrl = 'wss://stream.binance.com:9443/stream?streams='
                symbol_str+=symbol_str+'@bookTicker'
                symbol_str=baseUrl+symbol_str.strip('/') 
                print(symbol_str)
                ws = create_connection(symbol_str)
                while True:
                    data = ws.recv()
                    print(data)
                    time.sleep(0.5)

    def process_message(self,msg):
        print("symbol:"+str(msg['data']['s'])+"\nBid: "+str(msg['data']['b'])+"\nAsk: "+str(msg['data']['a']))  
        
    def buy_order(self,symbol,quantity,api_key,api_secret):
        try:
            print("symbol=========: ",symbol)
            print("quantity========",quantity)
            self.client = Client(api_key,api_secret)
            responsmsg = self.client.futures_coin_create_order(symbol=str(symbol),
                                    side="BUY",
                                    type="MARKET",
                                    recvWindow=5000,
                                    timestamp=int(time.time() *1000),
                                    quantity=int(quantity))
            print(responsmsg)
        except Exception as e:
            print(e)

    def sell_order(self,symbol,quantity,api_key,api_secret):
        try:
            print("symbol=========: ",symbol)
            print("quantity========",quantity)
            self.client = Client(api_key,api_secret)
            responsmsg = self.client.futures_coin_create_order(symbol=str(symbol),
                                    side="SELL",
                                    type="MARKET",
                                    recvWindow=5000,
                                    timestamp=int(time.time() *1000),
                                    quantity=int(quantity))
            print(responsmsg)
        except Exception as e:
            print(e)

        
# Bnb_Trade().socket_connect()