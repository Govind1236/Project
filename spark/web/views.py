from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello its working')
def about(request):
    return HttpResponse('This is about page')