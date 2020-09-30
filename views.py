from django.shortcuts import render,redirect
from django.http import HttpResponse
from CCS.models import Login
# Create your views here.

def signin(request):
	#print("hai")
	if request.method=="POST":
	       userid=request.POST['userid']
	       pwd=request.POST['pwd']
	       data=Login.objects.create(userid=userid,pwd=pwd)
	       return HttpResponse("success")
	return render(request,'CCS/signin.html')       

        
	