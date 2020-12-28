from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
class student_signup_form(UserCreationForm):
	ID_No = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Student ID No.' }),required=True,max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter first name'}),required=True,max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email ID'}),required=True,max_length=45)
	department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter department'}),required=True,max_length=30)
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=30)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=30)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),required=True,max_length=30)

	class Meta:
		model=User
		fields=('ID_No','first_name','last_name','email','department','username','password1','password2')

	def clean_confirm_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password != confirm_password:
			raise forms.ValidationError("Password Mismatch")
		return confirm_password



        		        