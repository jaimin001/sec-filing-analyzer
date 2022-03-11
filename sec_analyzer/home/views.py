from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'home.html')