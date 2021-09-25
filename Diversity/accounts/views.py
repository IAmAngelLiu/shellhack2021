from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

from .models import *
from .utils import get_plot
from .utils import get_plot1

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
	total = employees.count()
	total_race = total_black + total_indian + total_hispanic
	female_points = (total-total_female)*100
	black_points = (total-total_black)*100
	indian_points = (total-total_indian)*100
	hispanic_points = (total-total_hispanic)*100
	college_points = (total-total_college)*100

	x = ['female', 'black', 'indian', 'hispanic', 'firstcollege']
	y = [total_female, total_black, total_indian, total_hispanic, total_college]
	chart = get_plot(x, y)

	x1 = ['gender', 'race', 'education']
	y1 = [total_female/total, total_race/total, total_college/total]
	chart1 = get_plot1(x1, y1)
	
	return render(request, 'accounts/home.html', {'categories': categories, 'employees': employees, 'total_female': total_female, 'total_black': total_black, 
		'total_indian': total_indian, 'total_hispanic': total_hispanic, 'total_college': total_college, 'total': total, 'chart': chart, 'total_race': total_race, 
		'chart1': chart1, 'female_points': female_points, 'black_points': black_points, 'indian_points': indian_points, 'hispanic_points': hispanic_points, 'college_points': college_points})



# def return_graph():
# 	my_data = [total_female,total_black,total_indian]
# 	my_labels = 'female','black','indian',...
# 	plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
# 	plt.title('Chart')
# 	plt.axis('equal')
# 	plt.show()
	# imgdata = StringIO()
 #    data = imgdata.getvalue()
    # return data






