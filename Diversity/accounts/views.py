from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

from .models import *
from .utils import get_plot
from .utils import get_plot1
from .utils import get_plot2
from .utils import get_plot3
from .utils import get_plot4
from .utils import get_plot5
from .utils import get_plot6
from .utils import get_plot7
from .utils import comment_by_color
# Create your views here.



def home(request):
	categories = Points.objects.all()
	employees = Employee.objects.all()
	female = employees.filter(gender='Female')
	male = employees.filter(gender='Male')
	black = employees.filter(race='Black')
	white = employees.filter(race='White')
	asian = employees.filter(race='Asian')
	indian = employees.filter(race='American Indian')
	others = employees.filter(race='Others')
	hispanic = employees.filter(race='Hispanic')
	college = employees.filter(firstcollege='Yes')
	total_female = female.count()
	total_male = male.count()
	total_black = black.count()
	total_white = white.count() 
	total_asian = asian.count() 
	total_others = others.count() 
	total_indian = indian.count()
	total_hispanic = hispanic.count()
	total_college = college.count()
	total = employees.count()
	total_race = total_black + total_indian + total_hispanic
	gender_percent = format(total_female/total,'.2%')
	race_percent = format(total_race/total,'.2%')
	college_percent = format(total_college/total,'.2%')

	female_points = int((0.5-total_female/total)*100)*100
	race_points = int((0.5-total_race/total)*100)*100
	college_points = int((0.5-total_college/total)*100)*100
	max_points=female_points+race_points+college_points

	x = ['female', 'black', 'indian', 'hispanic', 'firstcollege']
	y = [total_female, total_black, total_indian, total_hispanic, total_college]
	chart = get_plot(x, y)

	x1 = ['gender', 'race', 'education']
	y1 = [total_female/total, total_race/total, total_college/total]
	chart1 = get_plot1(x1, y1)
	chart2 = get_plot2(x1, y1)
	chart3 = get_plot3(x1, y1)

	x2 = ['female', 'male']
	y2 = [total_female, total_male]
	chart4 = get_plot4(x2, y2)

	x3 = ['white', 'black', 'asian', 'indian', 'hispanic', 'others']
	y3 = [total_white, total_black, total_asian, total_indian, total_hispanic, total_others]
	chart5 = get_plot5(x3, y3)

	x4 = ['first college student', 'not first college student']
	y4 = [total_college, total-total_college]
	chart6 = get_plot6(x4, y4)

	chart7 = get_plot7(total_female/total, total_race/total, total_college/total)
	comment = comment_by_color(total_female/total, total_race/total, total_college/total)


	return render(request, 'accounts/home.html', {'categories': categories, 'employees': employees, 'total_female': total_female, 'total_black': total_black, 
		'total_indian': total_indian, 'total_hispanic': total_hispanic, 'total_college': total_college, 'total': total, 'chart': chart, 'total_race': total_race, 
		'chart1': chart1, 'female_points': female_points, 'race_points': race_points, 'college_points': college_points, 'max_points':max_points,
		 'chart2': chart2, 'chart3': chart3, 'total_male': total_male, 'chart4': chart4, 'chart5': chart5, 'chart6': chart6,
		'gender_percent':gender_percent, 'race_percent':race_percent, 'college_percent':college_percent, 'chart7': chart7, 'comment': comment })










