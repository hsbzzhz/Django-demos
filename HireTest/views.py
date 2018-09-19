from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.

def index(request):

    return render(request,'index.html',locals())

def search(request):

    return render(request,'search.html',locals())

def profile(request):

    return render(request,'profile.html',locals())

