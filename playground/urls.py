from django.urls import path
from . import views

#URL Config
urlpatterns = [
    path('hello/', views.hello),
    path('', views.home),
    path('add', views.add), 
]