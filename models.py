from django.db import models

# Create your models here.
class Login(models.Model):
     userid= models.CharField(max_length=50)
     pwd=models.CharField(max_length=8)     
class upload(models.Model):
	certificate_name=models.CharField(max_length=150)
	pdf=models.FileField(upload_to='certificate/pdfs',default='SOME STRING')

	def __str__(self):
		return self.certificate_name