from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q


# Create your views here.
def article_list(request):
	article = Article.objects.all().order_by('date')
	return render(request,"articles/article_list.html",{'articles':article} )

def article_search(request):
	query = request.GET.get('search-box')
	article = Article.objects.filter(Q(title__icontains=query))
	return render(request,"articles/article_list.html",{'articles':article} )

def article_detail(request,slug):
	#return HttpResponse(slug)
	var = Article.objects.get(slug=slug)
	return render(request,'articles/article_detail.html',{'article':var})

@login_required(login_url="/accounts/login")
def article_create(request):
	if request.method == 'POST':
		#as files dosent come on post request so it need to be retrieved seperately to be validated
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			#save article to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')

	else:
		form = forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form':form})