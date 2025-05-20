from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', views.CategoryViewset)

urlpatterns = [
    path('', include(router.urls)),
]