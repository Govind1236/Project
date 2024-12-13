from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from.models import Person
from django.template import loader
# Create your views here.
def home(request):
    list_result = Person.objects.all() #extract data from database
    context = {
    # temp = loader.get_template('Sparks/about.html')
       'list_result': list_result,
    }
    # return HttpResponse(temp.render(context,request))
    return render(request,'Sparks/index.html',context) #returning data view to home url /
def about(request):
    return render(request,'Sparks/about.html')
def contact(req):
    return HttpResponse("Its an contact page")
def Index(req):
    return HttpResponse("<h1> You are at index page </h1>")
def detail(request, person_id):
    # list = Person.objects.get(pk = person_id)
    list = get_object_or_404(Person, pk = person_id)
    context = {
        'list':list,
    }
    return render(request,'Sparks/detail.html', context)

 