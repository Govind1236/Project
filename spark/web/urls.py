from.import views
from django.urls import path

app_name = 'web'
urlpatterns = [
    #/home/
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('',views.Index,name='index'),
    #/home/1
    path('home/<int:person_id>/',views.detail,name='detail'),
    
]