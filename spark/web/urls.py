from.import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('',views.Index,name='index'),
    
]