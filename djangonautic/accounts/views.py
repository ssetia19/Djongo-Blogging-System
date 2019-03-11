from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.db.models import Q

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log the user in
			login(request,user)
			#difference between render and redirect
			return redirect('home')
	else:
		form = CustomUserCreationForm()
	return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
	#return HttpResponse("sagar")
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()
			login(request,user)
			if 'kittho_aaye_ho' in request.POST:
				return redirect(request.POST.get('kittho_aaye_ho'))
			else:
				return redirect('articles:list')
	else:
		form = AuthenticationForm()
	return render(request,"accounts/login.html",{'form':form})

def logout_view(request):
	#return HttpResponse("sagar")
	if request.method == 'POST':
		logout(request)
		return redirect('articles:list')

def profile_view(request):
	if request.method == 'POST':
		var = CustomUser.objects.filter(Q(username=request.user))
		return render(request,"accounts/profile.html",{'profiles':var } )
