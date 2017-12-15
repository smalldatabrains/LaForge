from map.models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
	queryset=MachineCategory.objects.values_list('category').distinct()
	serializer_class=CategorySerializer

