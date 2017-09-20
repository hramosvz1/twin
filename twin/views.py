from django.shortcuts import render
from .models import *
# Create your views here.

def about(request):
	return render(request, 'about-us.html', {})

def index(request):
	return render(request, 'index.html', {})

def activity(request):
	return render(request, 'activity.html', {})

def authoredit(request):
	return render(request, 'author-edit.html', {})

def authorlogin(request):
	return render(request, 'author-login.html', {})

def blogdos(request):
	return render(request, 'blog-2.html', {})

def blogtres(request):
	return render(request, 'blog-3.html', {})

def bdetaild(request):
	return render(request, 'blog-detail-2.html', {})

def bdetail(request):
	return render(request, 'blog-detail.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def contact(request):
	return render(request, 'contact-us.html', {})

def faq(request):
	return render(request, 'faq.html', {})

def grupos(request):
	return render(request, 'grupos.html', {})

def login(request):
	return render(request, 'login.html', {})

def messagesdos(request):
	return render(request, 'messages-2.html', {})

def messages(request):
	return render(request, 'messages.html', {})

def organization(request):
	return render(request, 'organization.html', {})

def page1(request):
	return render(request, 'page1.html', {})

def page2(request):
	return render(request, 'page2.html', {})

def page3(request):
	return render(request, 'page3.html', {})

def people(request):
	return render(request, 'people.html', {})

def search(request):
	return render(request, 'search.html', {})

def sitemap(request):
	return render(request, 'site-map.html', {})

def work(request):
	return render(request, 'work.html', {})

def author(request):
	return render(request, 'author.html', {})

def statictics(request):
	return render(request, 'statictics.html', {})

def shortcodes(request):
	return render(request, 'shortcodes.html', {})

def creargrupo(request):
	return render(request, 'crear_grupo.html', {})

def chat(request):
	return render(request, 'chat.html', {})





