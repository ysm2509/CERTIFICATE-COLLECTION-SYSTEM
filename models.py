from django.forms import ModelForm,Textarea
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Faculty(models.Model):
	name=models.CharField(max_length=30,default=False)
class FacLogin(models.Model):
	userid=models.CharField(max_length=20,default=False)
	pwd=models.CharField(max_length=8,default=False)

class Document(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 
