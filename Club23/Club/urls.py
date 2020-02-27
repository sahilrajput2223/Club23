from django.urls import path, include
from .views import  Home
app_name='Club'

urlpatterns = [
    path('', Home, name="home"),
]
