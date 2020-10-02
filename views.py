from django.shortcuts import render,redirect
from django.http import HttpResponse
from CCS.models import Login
from CCS.forms import DocumentForm 
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
			return redirect('uploadhtml')
	else :
		form=DocumentForm()
	return render(request,'CCS/uploadhtml.html',{'form':form})
	     		