from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [
	url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', logout,{'next_page': '/accounts/login'}),
]