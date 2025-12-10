from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def studentView(req):
    students = {
        'id': 1,
        'name':'Abhishek',
        'class':'cs'
    }
    return JsonResponse(students)