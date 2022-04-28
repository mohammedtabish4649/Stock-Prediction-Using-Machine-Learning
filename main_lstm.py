from pandas.core.frame import DataFrame
import pandas_datareader as pdr
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
import math
from sklearn.metrics import mean_squared_error
from numpy import array
import matplotlib.pyplot as plt

class lstm_logic():        
    def tinngo_dataReader(self,tinngo_symbol,api_key):
        self.symbol = tinngo_symbol
        self.api_key = api_key
        print('self.api_key: ', self.symbol)
        print('self.api_key: ',self.api_key)
        print("tinngo_dataReader")
        df = pdr.get_data_tiingo(str(self.symbol), api_key=str(self.api_key))
        df=df.reset_index()['close']
        return df

    

    def splitDS(self,df1):
        self.scaler=MinMaxScaler(feature_range=(0,1))
        df1=self.scaler.fit_transform(numpy.array(df1).reshape(-1,1))
        training_size=int(len(df1)*0.65)
        test_size=len(df1)-training_size
        train_data,test_data=df1[0:training_size,:],df1[training_size:len(df1),:1]
        return train_data,test_data,df1

    def create_dataset(self,dataset, time_step=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-time_step-1):
            a = dataset[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100 
            dataX.append(a)
            dataY.append(dataset[i + time_step, 0])
        return numpy.array(dataX), numpy.array(dataY)

    def modelGenerator(self,X_train,y_train,X_test,ytest,epochs):
        model=Sequential()
        model.add(LSTM(50,return_sequences=True,input_shape=(100,1)))
        model.add(LSTM(50,return_sequences=True))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error',optimizer='adam')
        print(model.summary())
        model.fit(X_train,y_train,validation_data=(X_test,ytest),epochs=epochs,batch_size=64,verbose=1)
        train_predict=model.predict(X_train)
        test_predict=model.predict(X_test)
        train_predict=self.scaler.inverse_transform(train_predict)
        test_predict=self.scaler.inverse_transform(test_predict) 
        print("Train Data RMSE: ",math.sqrt(mean_squared_error(y_train,train_predict)))
        print("Test Data RMSE: ",math.sqrt(mean_squared_error(ytest,test_predict)))
        return train_predict,test_predict,model

    def STP_plotting(self,df1,train_predict,test_predict):
        look_back=100
        trainPredictPlot = numpy.empty_like(df1)
        trainPredictPlot[:, :] = numpy.nan
        trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict
        # shift test predictions for plotting
        testPredictPlot = numpy.empty_like(df1)
        testPredictPlot[:, :] = numpy.nan
        testPredictPlot[len(train_predict)+(look_back*2)+1:len(df1)-1, :] = test_predict
        scaler_df1 = self.scaler.inverse_transform(df1)
        f2 = plt.figure()
        af2 = f2.add_subplot(111)
        
        af2.plot(self.scaler.inverse_transform(df1))
        af2.plot(trainPredictPlot)
        af2.plot(testPredictPlot)
        af2.set_title('Train/Test Predictions')
        plt.show(block=False)
        # return trainPredictPlot,testPredictPlot,scaler_df1
        # plot baseline and predictions
        # plt.plot(self.scaler.inverse_transform(df1))
        # plt.plot(trainPredictPlot)
        # plt.plot(testPredictPlot)
        # plt.show()
        # To do================================
    
    def prediction_for_next_10_days(self,test_data,model,df1):
        print("prediction_for_next_10_days")
        x_input=test_data[len(test_data)-100:].reshape(1,-1)
        # x_input.shape
        temp_input=list(x_input)
        temp_input=temp_input[0].tolist()
        lst_output=[]
        n_steps=100
        i=0
        while(i<30):
            
            if(len(temp_input)>100):
                #print(temp_input)
                x_input=numpy.array(temp_input[1:])
                # print("{} day input {}".format(i,x_input))
                x_input=x_input.reshape(1,-1)
                x_input = x_input.reshape((1, n_steps, 1))
                #print(x_input)
                yhat = model.predict(x_input, verbose=0)
                # print("{} day output {}".format(i,yhat))
                temp_input.extend(yhat[0].tolist())
                temp_input=temp_input[1:]
                #print(temp_input)
                lst_output.extend(yhat.tolist())
                i=i+1
            else:
                x_input = x_input.reshape((1, n_steps,1))
                yhat = model.predict(x_input, verbose=0)
                # print(yhat[0])
                temp_input.extend(yhat[0].tolist())
                # print(len(temp_input))
                lst_output.extend(yhat.tolist())
                i=i+1
    
        day_new=numpy.arange(1,101)
        day_pred=numpy.arange(101,131)
        f3 = plt.figure()
        af3 = f3.add_subplot(111)
        af3.plot(day_new,self.scaler.inverse_transform(df1[len(df1)-100:]))
        af3.plot(day_pred,self.scaler.inverse_transform(lst_output)) 
        af3.set_title('Prediction Curve')
        plt.show(block=False)
        # plt.show()
        f4 = plt.figure()
        af4 = f4.add_subplot(111)
        df3=df1.tolist()
        df3.extend(lst_output)
        df3 = df3[1200:]
        af4.plot(df3)
        af4.set_title('Joint 30 day Prediction')
        plt.show(block=False)
        print("done")
        plt.show()  
        
        # return df3
        
    def can1(self,dataFrame):
        f1 = plt.figure()
        af1 = f1.add_subplot(111)
        af1.plot(dataFrame)
        af1.set_title('5 Years of Data')
        plt.show(block=False)

    # def can2(self,df3):
    #     plt.figure(4)
    #     plt.subplot(215)
    #     plt.plot(df3)
        # plt.show()

    # def canvas_STP_plotting(self,data):
    #     fig = Figure(figsize = (5, 5),
    #              dpi = 50)
    
    #     # adding the subplot
    #     plot1 = fig.add_subplot(111)
    
    #     # plotting the graph
    #     plot1.plot(dataFrame)
    
    #     # creating the Tkinter canvas
    #     # containing the Matplotlib figure
    #     canvas = FigureCanvasTkAgg(fig,
    #                             master = frame)  
    #     canvas.draw()
    #     canvas.get_tk_widget().pack()
  
    #     toolbar = NavigationToolbar2Tk(canvas,frame)
    #     toolbar.update()
    
    #     # placing the toolbar on the Tkinter window
    #     canvas.get_tk_widget().pack()