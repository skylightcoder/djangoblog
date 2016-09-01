from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    data = {'mydata': "Hello world from my blog"}
    return render(request,'blog/index.html', data)
# Create your views here.
