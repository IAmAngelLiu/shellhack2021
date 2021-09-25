from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from .models import *

# Create your views here.

def home(request):
	categories = Points.objects.all()
	employees = Employee.objects.all()
	female = employees.filter(gender='Female')
	black = employees.filter(race='Black')
	indian = employees.filter(race='American Indian')
	hispanic = employees.filter(race='Hispanic')
	college = employees.filter(firstcollege='Yes')
	total_female = female.count()
	total_black = black.count()
	total_indian = indian.count()
	total_hispanic = hispanic.count()
	total_college = college.count()
	# categories = Points.objects.all()
	# categories = Employee.objects.all()
	# counting = Employee.objects.filter(gender='Female').count()
	return render(request, 'accounts/home.html', {'categories': categories, 'employees': employees, 'total_female': total_female, 'total_black': total_black, 'total_indian': total_indian, 'total_hispanic': total_hispanic, 'total_college': total_college})



