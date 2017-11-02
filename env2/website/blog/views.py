from django.shortcuts import render
from django.http import HttpResponse
from .models import post

# Create your views here.

def home(request):
	return HttpResponse("hello World")

def listview(request):
	objs = post.objects.all()
	return render(request,'index.html',{'posts':objs})
