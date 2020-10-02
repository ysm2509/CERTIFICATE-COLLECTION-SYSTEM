from django.forms import ModelForm,Textarea
from django.db import models

# Create your models here.
class Login(models.Model):
     userid= models.CharField(max_length=50,null=True)
     pwd=models.CharField(max_length=8,null=True)

#     def __str__(self):
#     	return self.userid


#class Upload(models.Model):
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 			     	