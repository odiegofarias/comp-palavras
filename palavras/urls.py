from django.urls import path
from . import views


app_name = "palavras"

urlpatterns = [
    path('', views.home, name='home'),
]
