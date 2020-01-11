from django.urls import path
from . import views

app_name = 'passwordgenerator'

urlpatterns = [
    path('', views.index, name='index')
]
