from django.shortcuts import render
from django.http.response import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from dividends.models import Company, Stock
from django.template import loader
from dividends.integration.dividends import email_transactions_reader
import imaplib
import os
import json
import email
import traceback
import datetime
import pprint
from django.core.exceptions import ImproperlyConfigured
import MyInvest.settings as settings

# Create your views here.
def index(request):
    companies_list = Company.objects.order_by('name')
    stocks_list = Stock.objects.all()
    new_transactions = read_email_from_gmail()
    template = loader.get_template('dividends/index.html')
    context = {
        'companies_list' : companies_list,
        'stocks_list' : stocks_list,
        'new_transactions' : new_transactions # List of transactions that occured the day before and that are received in the current day's statement
    }

    return HttpResponse(template.render(context, request))

def dividends_calendar(request):
    stocks_list = Stock.objects.all()
    template = loader.get_template('dividends/dividends_calendar.html')
    context = {
        'stocks_list' : stocks_list
    }

    return HttpResponse(template.render(context, request))

def read_email_from_gmail():
    try:
        settings_gmail = settings.EMAILS.get('gmail')
        
        mail = imaplib.IMAP4_SSL(settings_gmail.get('SMTP_SERVER'))
        mail.login(settings_gmail.get('FROM_EMAIL'),settings_gmail.get('FROM_PWD'))
        mail.select('inbox')
        
        new_transactions = []
        
        date = (datetime.date.today()).strftime("%d-%b-%Y")
        subject = settings.TRADING212_SUBJECT
        sender = settings.TRADING212_SENDER
        result, data = mail.search(None, '(SENTSINCE {date} FROM sender)'.format(date=date))
        
        print(data)
        
        for num in data[0].split():
            result, data = mail.fetch(num, '(RFC822)')
            print('Message: {0}\n'.format(num))
            pprint.pprint(data[0][1])
            
        mail.close()
        mail.logout()   
        
    except Exception as e:
        traceback.print_exc() 
        print(str(e))
    
with open(os.path.join(settings.BASE_DIR, 'parameters.json')) as parameters_file:
    parameters = json.load(parameters_file)

def get_email_subject(self, setting, parameters=parameters):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return parameters[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))  

def pieChart(request):
    template = loader.get_template('dividends/stocks_portfolio.html')
    stocks_list = Stock.objects.all()
    return render(request, 'dividends/stocks_portfolio.html',{'stocks_list' : stocks_list})

def chart():
    f = plt.figure()
    x = np.arange(10)
    h = [0,1,2,3,5,6,4,2,1,0]
    plt.title('Title')
    plt.xlim(0, 10)
    plt.ylim(0, 8)
    plt.xlabel('x label')
    plt.ylabel('y label')
    bar1 = plt.bar(x,h,width=1.0,bottom=0,color='Green',alpha=0.65,label='Legend')
    plt.legend()

    canvas = FigureCanvasAgg(f)    
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(f)  
