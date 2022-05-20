'''
Created on 14 May 2022

@author: mpayen
'''
import matplotlib
import matplotlib.pyplot as plt
from threading import Thread, Lock
from dividends.models import Stock

class Pie_Chart_Stocks(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Creating dataset
        lock = Lock()
        
        stocks = Stock.objects.all()
        stock_names = []
        company_names = []
        numbers_of_shares = []
        
        for stock in stocks:
            stock_names.append(stock.company.stock_name)
            company_names.append(stock.company.name)
            numbers_of_shares.append(stock.number_of_shares)
        
        print(stock_names)
        # Creating plot
        #fig = plt.figure(figsize =(10, 7))
        #axe = fig.add_subplot(111)
        #plt.pie(numbers_of_shares, labels = stock_names)
        # show plot
        #plt.show()
        print(stock_names)