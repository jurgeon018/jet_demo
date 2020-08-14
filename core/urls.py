from django.urls import path 

from django.shortcuts import render 

def index(request):
    return render(request, 'common/temp1.html', locals())


urlpatterns = [
    path('', index, name='index'),
]
