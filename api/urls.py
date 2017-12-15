from django.conf.urls import url,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'category',views.CategoryViewset)


urlpatterns = [
	url(r'^',include(router.urls)),

]