from .forms import *
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.files import File
import json
import os
from django.conf import settings


@login_required
def map(request):
	try:
		carte=Process.objects.latest('date_created')
		categories=MachineCategory.objects.values_list('category',flat=True).distinct()
		categories=list(categories)
		spares=SparePart.objects.all()
		return render(request,'map.html',{'categories':categories,'carte':carte})
	except Process.DoesNotExist:
		categories=MachineCategory.objects.values_list('category',flat=True).distinct()
		categories=list(categories)
		return render(request,'map.html',{'categories':categories})
	

@login_required
def addmaintenance(request):
	if request.method=="POST":
		date_start=request.POST.get('date_start')
		date_end=request.POST.get('date_end')
		machine=request.POST.get('machine')
		technician=request.POST.get('technician')
		spare_part=request.POST.get('spare_part')
		detail=request.POST.get('detail')

		Maintenance.objects.create(
			date_start=date_start,
			date_end=date_end,
			machine=machine,
			technician=technician,
			spare_part=spare_part,
			detail=detail
		)
		return HttpResponse('')

@login_required
def machine(request):
	machines=MachineCategory.objects.all()
	form = machineForm()
	return render(request,'machine.html',{'machines':machines,'form':machineForm})


@login_required
def addmachine(request):
	i=0
	if request.method=="POST":
		print("Data :")
		print(request.POST)
		print("File :")
		print(request.FILES)
		category=request.POST.get('category')
		supplier=request.POST.get('supplier')
		picture=request.FILES.get('picture',False)
		print("Picture")
		print(picture)
		sparepart=request.POST.get('spare_list[]')
		sparepart=json.loads(sparepart)
		print("Spare Parts :")
		print(sparepart)
		s=[]
		for spare in sparepart:
			print(spare)
			s.append(SparePart(name=spare))
			s[i].save()
			i=i+1
		m=MachineCategory(
			category=category,
			supplier=supplier,
			picture=picture,
			)
		m.save()
		for spare in s:
			m.sparepart.add(spare)

		return HttpResponseRedirect('../machine')



@login_required
def saveprocess(request):
	if request.method=="POST":
		process=request.POST.get('process')
		connections=request.POST.get('connections')
		nodes=request.POST.get('nodes')
		Process.objects.create(
			process=process,
			nodes=nodes,
			connections=connections
		)
		return HttpResponse('')


@login_required
def about(request):
	return render(request,'about.html')

@login_required
def report(request):
	dates=Maintenance.objects.values_list('date_start',flat=True)
	print(dates)
	maintenances=Maintenance.objects.all()
	return render(request,'report.html',{'maintenances':maintenances,'dates':dates})

@login_required
def history(request):
	return render(request,'history.html')
