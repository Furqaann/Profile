from django.urls import path
from task import views


urlpatterns = [
    path('', views.index,name='index'),
    path('Projects.html/', views.generic,name='projects'),
    path('Contact.html/', views.elements,name='contact'),
     
]