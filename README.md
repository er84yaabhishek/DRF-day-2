# DRF-day-2
Simple API Endpoint - API Development with Django REST Framework


git init
git remote add origin <your-github-repo-link>
git add .
git commit -m "Initial project setup"
git branch -M main
git push -u origin main , git push -f origin main
(
git pull origin main 
git push origin main
)

===============================
static data show in api end point 

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
