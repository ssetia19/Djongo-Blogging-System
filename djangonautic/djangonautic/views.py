from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	#return HttpResponse('this is homepage')
	return render(request,'homepage.html')

def about(request):
	#return HttpResponse("this is about page")
	return render(request,'about.html')