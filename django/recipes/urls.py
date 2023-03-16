from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<id>/', views.recipes),
]
