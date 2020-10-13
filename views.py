from django.shortcuts import render,redirect
from django.http import HttpResponse
from CCS.models import Login,Document
from CCS.forms import DocumentForm 
import csv
# Create your views here.
def base(request):
	return render(request,'CCS/base.html')
def signin(request):
	
	if request.method=="POST":
	       userid=request.POST['userid']
	       pwd=request.POST['pwd']
	       data=Login.objects.create(userid=userid,pwd=pwd)
	       return redirect('uploadhtml')
	return render(request,"CCS/signin.html")              

        
def uploadhtml(request):
	if request.method == 'POST':
		form=DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('showdocument')
	else :
		form=DocumentForm()
	return render(request,'CCS/uploadhtml.html',{'form':form})

def exportcsv(request):
	details=Login.objects.all()
	response=HttpResponse('text/csv')
	response['Content-Disposition']='attachment;filename=login.csv'
	writer=csv.writer(response)
	writer.writerow(['userid','pwd'])
	fields=details.values_list('userid','pwd')
	for i in fields:
		writer.writerow(i)
	return response	
def showlogin(request):
	logins=Login.objects.all()
	return render(request,"CCS/showlogin.html",{'login':logins})

def showdocument(request):
	docs=Document.objects.all()
	return render(request,"CCS/showdocument.html",{'document':docs})

