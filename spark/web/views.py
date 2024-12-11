from django.shortcuts import render
from django.http import HttpResponse
from.models import Person
from django.template import loader
# Create your views here.
def home(request):
    list_result = Person.objects.all() #extracting data from database 
    template = loader.get_template('Sparks/index.html')
    context = {
        'list_result': list_result,
    }
    return HttpResponse (template.render(context,request))  #returning data view to home url /
def about(request):
    # list_result = Person.objects.all()
    # temp = loader.get_template('Sparks/about.html')
    # context = {
    #    'list_results': list_result,
    # }
    return render(request, 'Sparks/about.html')
def contact(req):
    return HttpResponse("Its an contact page")
def Index(req):
    return HttpResponse("<h1> You are at index page </h1>")

 