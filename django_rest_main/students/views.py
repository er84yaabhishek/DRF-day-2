from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(req):
    return HttpResponse('<h1>soft84ya</h1>')