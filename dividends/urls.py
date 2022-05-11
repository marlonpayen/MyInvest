from django.urls import path
from dividends import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('pie chart', views.pieChart, name='pie chart'),

]