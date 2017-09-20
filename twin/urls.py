from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$', views.index),
#	url(r'^about/$', views.about),
#	url(r'^activity/$', views.activity),
	url(r'^author-edit/$', views.authoredit),
	url(r'^author-login/$', views.authorlogin),
#	url(r'^author/$', views.author),
#	url(r'^blog-2/$', views.blogdos),
	url(r'^blog-3/$', views.blogtres),
	url(r'^grupo/$', views.blogtres),
#	url(r'^blog-detail-2/$', views.bdetaild),
	url(r'^blog-detail/$', views.bdetail),
#	url(r'^blog/$', views.blog),
	url(r'^contact/$', views.contact),
	url(r'^faq/$', views.faq),
	url(r'^grupos/$', views.grupos),
#	url(r'^login/$', views.login),
#	url(r'^messages-2/$', views.messagesdos),
	url(r'^messages/$', views.messages),
#	url(r'^organization/$', views.organization),
	url(r'^page1/$', views.page1),
#	url(r'^page2/$', views.page2),
#	url(r'^page3/$', views.page3),
	url(r'^people/$', views.people),
	url(r'^search/$', views.search),
#	url(r'^site-map/$', views.sitemap),
	url(r'^work/$', views.work),
#	url(r'^statictics/$', views.statictics),
#	url(r'^short-codes/$', views.shortcodes),
	url(r'^crear-grupo/$', views.creargrupo),
	url(r'^chat/$', views.chat),
]