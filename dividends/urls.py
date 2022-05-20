from django.urls import path
from dividends import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('dividends_calendar', views.dividends_calendar, name='dividends_calendar'),
    path('pie chart', views.pieChart, name='pie chart'),

]