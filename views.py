from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from CCS.models import FacLogin,Document
from CCS.forms import *
import csv
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.http import require_http_methods
# Create your views here.
def base(request):
	return render(request,'CCS/base.html')

def student_signup(request):
	if request.method=='POST':
		form = student_signup_form(request.POST)
		if form.is_valid():
			print("valid")
			user=form.save()
			return HttpResponse("Successfull")
	else:
		form=student_signup_form()
	return render(request,"CCS/student_signup.html",{'form':form})
def signin(request):
	if request.method=="POST":
	       username=request.POST['username']
	       password=request.POST['password']
	       user = authenticate(username=username,password=password)
	       if user is not None :
	       	 login(request,user)
	       	 return redirect('student_dashboard')
	       else :
	       	return redirect('loginerror')

	return render(request,"CCS/signin.html")  


@login_required(login_url="/signin")
def uploadhtml(request):
	if request.method == 'POST':
		form=DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.userid=request.user
			instance.save()
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
	logins=User.objects.all()
	return render(request,"CCS/showlogin.html",{'login':logins})
#@login_required("/signin")
def showdocument(request):
	try :
		docs=Document.objects.filter(userid=request.user) 
		return render(request,"CCS/showdocument.html",{'document':docs})
	except:
		return redirect('student_dashboard')
def loginerror(request):
	return render(request,"CCS/loginerror.html")
def facerror(request):
	return render(request,"CCS/facerror.html")
def faclogin(request):
	if request.method=="POST":
		userid=request.POST['userid']
		pwd=request.POST['pwd']
		try:
			fac=Faculty.objects.get(name=userid)
			if fac.name==userid:
				user = authenticate(username=userid,password=pwd)
				if user is not None :
					login(request,user)
					return redirect('facdata')
				else :
					return redirect('facerror')
		except :
			return HttpResponse("Not a valid user")
	return render(request,"CCS/faclogin.html")
def base1(request):
	return render(request,"CCS/base1.html")

@login_required(login_url="/faclogin")
def facdata(request):
	if request.method=="POST":
		username=request.POST['username']
		ds=User.objects.get(username=username,)
		print(ds)
		docs=Document.objects.filter(userid=ds.id)
		print(docs)
		return render(request,"CCS/facdata.html",{'document':docs})
	return render(request,"CCS/facdata.html")

def fac_data_fail(request):
	return render(request,"CCS/fac_data_fail.html")
def student_dashboard(request):
	return render(request,"CCS/student_dashboard.html")
#@login_required("/signin")
def user_logout(request):
	logout(request)
	return redirect('base')






