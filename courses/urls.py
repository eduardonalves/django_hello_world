from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.index, name='index'),
    path('duvidas', views.duvidas, name='duvidas'),
    #path('details/<int:id>', views.details, name='details'),
    path('details/<slug:slug>', views.details, name='details'),
    
    
]