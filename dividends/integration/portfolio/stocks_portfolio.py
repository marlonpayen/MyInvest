'''
Created on 2 May 2022

@author: mpayen
'''
from django.shortcuts import render

class Stocks_Portfolio(object):
    '''
    classdocs
    '''


    def __init__(self, file):
        '''
        Constructor
        '''
        self.file = file
    
    
    def read_file(self, request):
        if request.method == "POST":
            my_uploaded_file = request.FILES['portfolio_file'].read() # get the uploaded file
            # do something with the file
            for i in my_uploaded_file:
                print(i)
            # and return the result  
            return my_uploaded_file          
        else:
            return render(request, 'dividends/index.html')

        