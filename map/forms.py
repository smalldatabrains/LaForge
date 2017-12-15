from django import forms

from .models import *

#Machine Page

class machineForm(forms.ModelForm):
	category=forms.CharField(widget=forms.TextInput(attrs={'class':'form-right','placeholder':'Category'}))
	supplier=forms.CharField(widget=forms.TextInput(attrs={'class':'form-right','placeholder':'Supplier'}))
	picture=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-right','name':'picture'}))
	spare_part=forms.CharField(widget=forms.Textarea(attrs={'class':'form-right','id':'sparelist'}))
	class Meta:
		model=MachineCategory
		fields=('category','supplier','picture','spare_part')
		

class maintenanceForm(forms.ModelForm):
	date_start=forms.DateField(widget=forms.DateInput(attrs={'class':'date','placeholder':'Start Date'}))
	date_end=forms.DateField(widget=forms.DateInput(attrs={'class':'date','placeholder':'End Date'}))
	technician=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Technician'}))
	machine=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Machine'}))
	spare_part=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Spare part'}))
	class Meta:
		model=Maintenance
		fields=('date_start','date_end','technician','machine','spare_part')

