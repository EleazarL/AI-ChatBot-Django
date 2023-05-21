from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('specific',views.specific,name='specific'),
    
    #ruta para obtener la respuestas 
    path('chat/getResponse', views.getResponse, name='getResponse'),]
