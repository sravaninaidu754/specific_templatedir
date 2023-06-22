from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'virat.html')

def venky(request):
    return HttpResponse('<h1>THIS IS VENKY STRING RESPONSE</h1>')