from django.db import models
from django.contrib.auth.models import User

class SparePart(models.Model):
	name=models.CharField(max_length=30,primary_key=True)
	def __str__(self):
		return self.name

class MachineCategory(models.Model):
    category=models.CharField(max_length=30)
    supplier=models.CharField(max_length=30)
    picture=models.ImageField()
    sparepart=models.ManyToManyField(SparePart)
    def __str__(self):
    	return self.category


class Maintenance(models.Model):
	date_start=models.DateField(null=True)
	date_end=models.DateField(null=True)
	technician=models.CharField(max_length=30,null=True)
	machine=models.CharField(max_length=30,null=True)
	sparePart=models.CharField(max_length=30,null=True)
	detail=models.TextField(null=True)

class Process(models.Model):
	process=models.TextField(null=True)
	connections=models.TextField(null=True)
	nodes=models.TextField(null=True)
	date_created=models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
