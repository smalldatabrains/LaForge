from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.map,name='map'),
    url(r'^machine/$', views.machine,name='machine'),
    url(r'^about/$', views.about,name='about'),
    url(r'^history/$', views.history,name='history'),
    url(r'^report/$', views.report,name='report'),
    url(r'^addmaintenance/$', views.addmaintenance,name='addmaintenance'),
    url(r'^addmachine/$', views.addmachine,name='addmachine'),
    url(r'^saveprocess/$', views.saveprocess,name='saveprocess'),
    
]
