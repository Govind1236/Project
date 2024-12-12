from.import views
from django.urls import path

urlpatterns = [
    #/home/
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.Index,name='index'),
    #/home/1
    path('detail/<int:person_id>/',views.detail,name='detail'),
    
]