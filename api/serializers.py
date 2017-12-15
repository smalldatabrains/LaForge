from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from map.models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=MachineCategory
		fields=('category',)

