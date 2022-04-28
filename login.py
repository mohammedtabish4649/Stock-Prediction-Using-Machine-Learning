from tkinter import *
import os
from main_lstm import lstm_logic
from tkinter import * 
import matplotlib.pyplot as plt
from binance_lib import Bnb_Trade
import threading


class MainScreen(lstm_logic,Bnb_Trade):
    def __init__(self):
        self.live_feed_thread = ''
        self.root = Tk()
        self.root.geometry("1350x700+0+0")
        self.root.title("Binance Trader")
        self.root.configure(background='#2f6275')
        self.root.resizable(False,False)
        self.fg_bg = '#2f6275'

        self.bg = self.root.configure(bg=self.fg_bg)        
        # index Frame

        self.indexPage = Frame(self.root,bg=self.fg_bg)
        self.indexPage.place(x=450,y=250,height=250,width=350)

        # Header Frame and label
        self.HeaderFrame = Frame(self.indexPage)
        self.HeaderFrame.pack(side=TOP,fill='x')
        self.Header = Label(self.indexPage,text="Index Page",font=("Impact",35,"bold"),fg=self.fg_bg,bg='white')
        self.Header.pack(side=TOP)

        # Login button
        self.loginBtn = Button(self.indexPage,text="Login",width=12,command=self.loginpage)     
        self.loginBtn.place(x=60,y=95)

        # Register button
        self.registerBtn = Button(self.indexPage,text="Register",width=12,command=self.registrationPage)
        self.registerBtn.place(x=60,y=125)
        self.count = StringVar()
        self.count = "indexPage"
        self.root.mainloop()

    def loginpage(self):
        if self.count == 'Frame_register':
            self.Frame_register.destroy()
        if self.count == 'indexPage':
            self.indexPage.destroy()
            
        self.count = 'Frame_login'
        

        self.Frame_login = Frame(self.root,bg="white")
        self.Frame_login.place(x=150,y=150,height=340,width=500)
        self.loginUsername = StringVar()
        self.loginPassword = StringVar()
        self.title = Label(self.Frame_login,text="Login Here",font=("Impact",35,"bold"),fg=self.fg_bg,bg="white").place(x=90,y=30 )
        self.desc = Label(self.Frame_login,text="User login Area",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=90,y=100)
        
        self.lbl_username = Label(self.Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.text_user = Entry(self.Frame_login,font=('times new roman',15),bg='lightgray',textvariable = self.loginUsername)
        self.text_user.place(x=90,y=170,width=350,height=35)

        self.lbl_password = Label(self.Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.text_pass = Entry(self.Frame_login,font=('times new roman',15),bg='lightgray',textvariable = self.loginPassword)
        self.text_pass.place(x=90,y=240,width=350,height=35)

        

        self.register_btn = Button(self.Frame_login,text="Register",width=12,font=("Goudy old style",15,"bold"),fg="gray",bg="white",command=self.registrationPage)
        self.register_btn.place(x=90,y=280)
        
        
        self.login_btn = Button(self.Frame_login,text="Login",width=12,font=("Goudy old style",15,"bold"),fg="gray",bg="white",command=self.checkCreds).place(x=250,y=280)
        


    def checkCreds(self):
        print("checkCreds")

        print(self.text_user.get(), self.text_pass.get())
        # if self.text_user =='' or self.text_pass =='':
        #     self.c = Label(self.Frame_login,text='Invalid Credentials',font=("Goudy old style",15,"bold"),fg="red",bg="white")
        #     self.c.place(x=90,y=300)
        #     print(self.c.cget('text'))
        # if self.c.cget('text')=='Invalid Credentials':
        #     self.c.destroy()

        # username_entry1.delete(0, END)
        # password_entry1.delete(0, END)
        os.chdir(r'G:\project_msc\login_UI\login_UI\users')
        list_of_files = os.listdir()
        if self.text_user.get() in list_of_files:
            print("yes")
            file1 = open(self.text_user.get(), "r")
            self.verify = file1.read().splitlines()
            print(self.verify)
            if self.text_pass.get() in self.verify[1]:
                self.api_key = self.verify[2]
                self.api_secret = self.verify[3]
                self.tinngo_api_secret = self.verify[4]
                self.backTestingPage()
            else:
                self.password_not_recognised()
        else:
            print("user_not_found()")


    def login_sucess(self):
        print("Login Success")

    def password_not_recognised(self):
        print("User Not Found")

    def registrationPage(self):
        if self.count == 'indexPage':
            self.indexPage.destroy()
        if self.count == 'Frame_login':
            self.Frame_login.destroy()
        
        self.count = 'Frame_register'

        # Frame register
        self.Frame_register = Frame(self.root,bg="white")
        self.Frame_register.place(x=150,y=100,height=580,width=500)

        # Back button
        self.topFrame = Frame(self.Frame_register,bg="white")
        self.topFrame.pack(side=TOP,fill='x')
        self.backBtn = Button(self.topFrame,text="Back",command=self.loginpage).pack(side=LEFT)

        # Defining variables
        self.username = StringVar()
        self.password = StringVar()
        self.api_key = StringVar()
        self.api_secret = StringVar()
        self.tinngo_api_secret = StringVar()
        # Register Page content
        Label(self.Frame_register,text="Register Here",font=("Impact",35,"bold"),fg=self.fg_bg,bg="white").place(x=90,y=30 )
        Label(self.Frame_register,text="User Registration Area",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=90,y=100)

        Label(self.Frame_register,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.text_user = Entry(self.Frame_register,font=('times new roman',15),bg='lightgray',textvariable=self.username)
        self.text_user.place(x=90,y=170,width=350,height=35)

        Label(self.Frame_register,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.text_user = Entry(self.Frame_register,font=('times new roman',15),bg='lightgray',textvariable=self.password)
        self.text_user.place(x=90,y=240,width=350,height=35)

        Label(self.Frame_register,text="Api Key",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=280)
        self.text_user = Entry(self.Frame_register,font=('times new roman',15),bg='lightgray',textvariable=self.api_key)
        self.text_user.place(x=90,y=310,width=350,height=35)

        Label(self.Frame_register,text="Api Secret",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=350)
        self.text_user = Entry(self.Frame_register,font=('times new roman',15),bg='lightgray',textvariable=self.api_secret)
        self.text_user.place(x=90,y=380,width=350,height=35)

        Label(self.Frame_register,text="Tinngo Api Secret",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=420)
        self.text_user = Entry(self.Frame_register,font=('times new roman',15),bg='lightgray',textvariable=self.tinngo_api_secret)
        self.text_user.place(x=90,y=450,width=350,height=35)

        self.btn_register = Button(self.Frame_register,text="Register",font=("Goudy old style",15,"bold"),fg="gray",bg="white",command = self.registerUser).place(x=90,y=490)

        if self.btn_register:
            print(self.btn_register)

    def registerUser(self):
        os.chdir(r'D:\Users\AADITYA\Desktop\login_UI\users')

        self.username = self.username.get() 
        self.password = self.password.get()
        self.api_key = self.api_key.get()
        self.api_secret = self.api_secret.get()
        self.tinngo_api_secret = self.tinngo_api_secret.get()
        
        # if self.username == "":
        #     print(input)
        #     return 'Username Field is required'
        

        file = open(self.username, "w")
        file.write(self.username + "\n")
        file.write(self.password + "\n")
        file.write(self.api_key+ "\n")
        file.write(self.api_secret+ "\n")
        file.write(self.tinngo_api_secret + "\n")
        file.close()

        self.username = ''
        self.password = ''
        # self.api_key = ''
        # self.api_secret = ''
        # self.tinngo_api_secret = ''
        self.loginpage()

    def backTestingPage(self):  
        print('inside backteting')
        if self.count == 'Frame_login':
            self.Frame_login.destroy()
        self.count = 'Frame_backTestingPage'
        self.Frame_backTestingPage = Frame(self.root,bg='white')
        self.Frame_backTestingPage.place(x=150,y=100,height=350,width=500)
        self.backTestingPageHeader = Label(self.Frame_backTestingPage,text="Back-Testing Window",font=("Impact",25,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=20)
        self.backTestingPagedesc = Label(self.Frame_backTestingPage,text="Back-Testing Area",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=70)

        self.tinngoLabel = Label(self.Frame_backTestingPage,text="Enter Symbol",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=115)
        self.TinngoSymbol = Entry(self.Frame_backTestingPage,font=('times new roman',15),bg='lightgray') 
        self.TinngoSymbol.place(x=30,y=145,width=350,height=30)

        self.EpochLabel = Label(self.Frame_backTestingPage,text="Enter Number of Epochs",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=190)
        self.EpochEntry = Entry(self.Frame_backTestingPage,font=('times new roman',15),bg='lightgray')
        self.EpochEntry.place(x=30,y=220,width=350,height=30)

        self.quoteBtn = Button(self.Frame_backTestingPage,text="Submit",width=12,command=self.symbolQuote)
        self.quoteBtn.place(x=30,y=270)

        self.something = Button(self.Frame_backTestingPage,text="Trade",width=12,command=self.Trade)
        self.something.place(x=135,y=270)
        

    def symbolQuote(self):
        self.TinngoSymbol = self.TinngoSymbol.get()
        self.EpochEntry = self.EpochEntry.get() 
        api_key = self.tinngo_api_secret
        print("self.TinngoSymbol: ",self.TinngoSymbol)
        print("tinngo_api_secret",api_key)
        dataFrame = self.tinngo_dataReader(tinngo_symbol=self.TinngoSymbol,api_key=api_key)
        print(dataFrame)
        self.can1(dataFrame)
        # plt.plot(dataFrame)
        # print(dataFrame)
        
        train_data,test_data,df1 = self.splitDS(dataFrame)
        # print("train_data: ",train_data,"test_data: ",test_data)
        print("after train_data,test_data")
        time_step = 100
        X_train, y_train = self.create_dataset(train_data, time_step)
        X_test, ytest = self.create_dataset(test_data, time_step)
        print("after create_dataset")
        X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
        X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)
        print("after reshape")
        train_predict,test_predict,model = self.modelGenerator(X_train,y_train,X_test,ytest,int(self.EpochEntry))
        print("After modelGenerator: ")
        self.STP_plotting(df1,train_predict,test_predict) #To do =======================
        print("after STP_plotting")

        self.prediction_for_next_10_days(test_data,model,df1)
        
        
        # print("prediction_for_next_10_days:",day_new,day_pred,scalInv_day_new,scalInv_day_pred,full_op)



    def Trade(self):
        if self.count == 'Frame_backTestingPage':
            self.Frame_backTestingPage.destroy()
            
        self.Trading_Binance = Frame(self.root,bg='white')
        self.Trading_Binance.place(x=150,y=100,height=400,width=500)

        self.Trading_BinancePageheader = Label(self.Trading_Binance,text="Binance Trader Window",font=("Impact",25,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=20)
        self.Trading_BinancePageDesc = Label(self.Trading_Binance,text="Binance Trading Area",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=70)


        self.LabelSymbolBinance = Label(self.Trading_Binance,text="Enter Symbol",font=("Goudy old style",15,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=115)
        self.EntrySymbolBinance = Entry(self.Trading_Binance,font=('times new roman',15),bg='lightgray') 
        self.EntrySymbolBinance.place(x=30,y=145,width=200,height=30)
        self.DropDownSymbols()        
        symSubmitBtn = Button(self.Trading_Binance , text = "StartSocket" , command = self.show )
        symSubmitBtn.place(x = 30,y = 185,width=75,height=30)

        stopSocketBtn = Button(self.Trading_Binance , text = "StopSocket" , command = self.stopSocket )
        stopSocketBtn.place(x=120,y = 185,width=75,height=30) 
        self.Trading_BinanceBuySell = Label(self.Trading_Binance,text="Binance Buy/Sell Area",font=("Goudy old style",13,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=225)
        self.Trading_BinanceBuySellQty = Label(self.Trading_Binance,text="Enter Quantity",font=("Goudy old style",13,"bold"),fg=self.fg_bg,bg="white").place(x=30,y=250)

        self.Quantity = Entry(self.Trading_Binance,font=('times new roman',15),bg='lightgray') 
        self.Quantity.place(x=30,y=275,width=200,height=30)
        self.Quantity.insert(0,'1')

        BuyBtn = Button(self.Trading_Binance , text = "BUY" , command = lambda:self.buy_order(self.EntrySymbolBinance.get(),self.Quantity.get(),self.api_key,self.api_secret))
        BuyBtn.place(x=30,y = 315,width=75,height=30)

        SellBtn = Button(self.Trading_Binance , text = "SELL" , command = lambda:self.sell_order(self.EntrySymbolBinance.get(),self.Quantity.get(),self.api_key,self.api_secret))
        SellBtn.place(x=120,y = 315,width=75,height=30)

        

    def DropDownSymbols(self):
        drop_down_list_of_symbols = self.trade(self.api_key,self.api_secret)
        self.clicked = StringVar()
        drop = OptionMenu(self.Trading_Binance , self.clicked , *drop_down_list_of_symbols )
        drop.place(x=235,y=145,width=100,height=30)
    
    def show(self):
        print('show')
        self.EntrySymbolBinance.delete(0,'end')
        text = self.clicked.get()
        self.EntrySymbolBinance.insert(0,text)
        # self.socket_manager(str(text))
        if self.live_feed_thread == '':
            self.live_feed_thread = threading.Thread(target=self.socket_connect)
            self.live_feed_thread.start()
        else:
            self.socket='open'
            self.socket_connect(str(text))
        
        
    def stopSocket(self):
        print("open=============================")
        self.bm.stop_socket(self.conn_key)
        self.bm.close()
    


MainScreen()
