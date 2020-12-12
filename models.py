from django.forms import ModelForm,Textarea
from django.db import models
# Create your models here.
BRANCH_CHOICES=(
	('cse','CSE'),
	('ece','ECE'),
	('eee','EEE'),
	('it','IT'),
	)
class Login(models.Model):
     userid= models.CharField(max_length=15,null=False,primary_key=True,default='None')
     name=models.CharField(max_length=40,null=False)
     branch=models.CharField(max_length=3,choices=BRANCH_CHOICES,default=None)
     pwd=models.CharField(max_length=8,null=True)

#     def __str__(self):
#     	return self.userid

class FacLogin(models.Model):
	userid=models.CharField(max_length=15,null=False)
	name=models.CharField(max_length=40,null=False)
	pwd=models.CharField(max_length=8,null=True)

class Document(models.Model):
    userid=models.ForeignKey(Login,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 
