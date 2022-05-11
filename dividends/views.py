from django.shortcuts import render
from django.http.response import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from dividends.models import Company
from django.template import loader
from dividends.integration.portfolio.stocks_portfolio import Stocks_Portfolio

# Create your views here.
def index(request):
    companies_list = Company.objects.order_by('name')
    template = loader.get_template('dividends/index.html')
    context = {
        'companies_list': companies_list,
    }
    
    # read the browsed file with all the stocks bought/sold
    stocks_portfolio = Stocks_Portfolio.read_file(context, request)
    
    return HttpResponse(template.render(context, request))

def calendar(request):
    response = "calendar"
    return HttpResponse(response)

def pieChart(request):
    response = "pie chart"
    return HttpResponse(response)

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
