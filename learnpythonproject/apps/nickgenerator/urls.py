from django.urls import path
from . import views

app_name = 'nickgenerator'

urlpatterns = [
    path('', views.index, name='index')
]
