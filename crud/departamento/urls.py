from django.urls import path
from . import views

URLPATTERNS = [
    path('', views.index)
]
