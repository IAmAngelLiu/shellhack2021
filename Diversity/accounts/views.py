from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

from .models import *
from .utils import get_plot

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

	x = ['female', 'black', 'indian', 'hispanic', 'firstcollege']
	y = [total_female, total_black, total_indian, total_hispanic, total_college]
	chart = get_plot(x, y)
	
	return render(request, 'accounts/home.html', {'categories': categories, 'employees': employees, 'total_female': total_female, 'total_black': total_black, 'total_indian': total_indian, 'total_hispanic': total_hispanic, 'total_college': total_college, 'total': total, 'chart': chart})



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






