from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello client public api")

# Create your views here.
