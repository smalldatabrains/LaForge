from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('machine/', views.machine, name='machine'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('report/', views.report, name='report'),
    path('addmaintenance/', views.addmaintenance, name='addmaintenance'),
    path('addmachine/', views.addmachine, name='addmachine'),
    path('saveprocess/', views.saveprocess, name='saveprocess'),
]
