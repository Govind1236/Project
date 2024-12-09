from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello its working')
def about(request):
    return HttpResponse('This is about page')
def contact(req):
    return HttpResponse("Its an contact page")

 