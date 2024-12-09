from.import views
from django.urls import path

urlpatterns = [
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),

]