from django.shortcuts import render
from django.http import HttpResponse
from .models import School


def index(request):
	schools = School.objects.all()
	if request.POST:
		name = request.POST.get('name')
		School.objects.create(name=name)

		schools = School.objects.all()

	return render(request, 'schools.html', {'schools':schools})

