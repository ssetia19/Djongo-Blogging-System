from django.conf.urls import url
from . import views

#namespacing
app_name = 'articles'

urlpatterns = [
    #r means raw string
 	url(r'^$',views.article_list, name ="list"),
 	url(r'^article_search$',views.article_search, name ="search"),
 	url(r'^create/$',views.article_create,name="create"),
 	#below is a name capturing group ?P<name of thing we want to capture>   
 	url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail"),
 ]
