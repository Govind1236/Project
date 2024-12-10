from django.shortcuts import render
from django.http import HttpResponse
from.models import Person
# Create your views here.
def home(request):
    list_result = Person.objects.all() #extracting data from database 
    return HttpResponse (list_result)  #returning data view to home url /
def about(request):
    return HttpResponse('This is about page')
def contact(req):
    return HttpResponse("Its an contact page")
def Index(req):
    return HttpResponse("<marquee><h1> You are at index page </h1> </marquee>")

 