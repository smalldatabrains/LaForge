from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    re_path(r'^accounts/login/$', LoginView.as_view(template_name='admin/login.html'), name='login'),
    re_path(r'^accounts/logout/$', LogoutView.as_view(next_page='/accounts/login'), name='logout'),
]