from django import forms


# Everything that I need to retrieve and save to DB

class ConnexionForm(forms.Form):
	username=forms.CharField(label="Username",max_length=30)
	password=forms.CharField(label="Password",widget=forms.PasswordInput)

