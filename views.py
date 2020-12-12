from django.shortcuts import render,redirect
from django.http import HttpResponse
from CCS.models import Login,Document,FacLogin
from CCS.forms import DocumentForm 
import csv
# Create your views here.
def base(request):
	return render(request,'CCS/base.html')
def signin(request):
	
	if request.method=="POST":
	       userid=request.POST['userid']
	       pwd=request.POST['pwd']
	       try :
	          data=Login.objects.get(userid=userid,pwd=pwd)
	          return request('CCS/uploadhtml.html',{'form':form})
	       except :
	       	  return redirect('loginerror')
	return render(request,"CCS/signin.html")              

        
def uploadhtml(request):
	if request.method == 'POST':
		form=DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.userid=request.Login.userid
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
	logins=Login.objects.all()
	return render(request,"CCS/showlogin.html",{'login':logins})

def showdocument(request):
	docs=Document.objects.all()   
	return render(request,"CCS/showdocument.html",{'Document':docs})
def loginerror(request):
	return render(request,"CCS/loginerror.html")
def facerror(request):
	return render(request,"CCS/facerror.html")
def faclogin(request):
	if request.method=="POST":
		userid=request.POST['userid']
		pwd=request.POST['pwd']
		try:
			data=FacLogin.objects.get(userid=userid,pwd=pwd)
			return HttpResponse('suss')
		except :
			return render(request,"CCS/facerror.html")
	return render(request,"CCS/faclogin.html")
def base1(request):
	return render(request,"CCS/base1.html")
def facdata(request):
	if request.method=='POST':
		userid=request.POST['userid']
		try :
			data=Login.objects.get(userid=userid)
			return HttpResponse("Sucss")
		except:
			return redirect('fac_data_fail')


	return render(request,"CCS/facdata.html")

def fac_data_fail(request):
	return render(request,"CCS/fac_data_fail.html")







