from django.urls import path
from . import views

urlpatterns = [
    path('ayo/', views.ayo, name='ayo'),
]