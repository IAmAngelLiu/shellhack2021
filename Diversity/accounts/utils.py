import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from matplotlib import colors as mcolors
import matplotlib.cm as cm

def get_graph():
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek(0)
	image_png = buffer.getvalue()
	graph = base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	buffer.close()
	return graph



def get_plot(x, y):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	plt.title('Diversity Pie Chart')
	plt.pie(y,labels=x,autopct='%1.1f%%')
	plt.xticks(rotation=45)
	plt.xlabel('category')
	# plt.ylabel('count')
	plt.tight_layout()
	graph = get_graph()
	return graph


def get_plot1(x, y):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	plt.title('Chart')
	my_colors = ['red','blue','green']
	plt.pie(y,labels=x,colors=my_colors, autopct='%1.1f%%')
	plt.xticks(rotation=45)
	plt.xlabel('category')
	plt.ylabel('count')
	plt.tight_layout()
	graph = get_graph()
	return graph




def get_plot2(x, y):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	maxvalue = max(y[0], y[1], y[2])
	minvalue = min(y[0], y[1], y[2])
	if maxvalue == minvalue:
		my_colors = ['mistyrose']
		title = "Perfect Distribution in Gender, Race, and Education"
	elif maxvalue-minvalue < 0.2 and maxvalue-minvalue > 0 and maxvalue-minvalue == 0.2:
		my_colors = ['peachpuff']
		title = "Great Distribution in Gender, Race, and Education"
	elif maxvalue-minvalue < 0.5 and maxvalue-minvalue > 0.2 and maxvalue-minvalue == 0.5:
		my_colors = ['peachpuff']
		title = "Fairly Good Distribution in Gender, Race, and Education"
	elif maxvalue-minvalue > 0.5:
		my_colors = ['peachpuff']
		title = "Need Improvements in Distribution in Gender, Race, and Education"

	return title



def get_plot3(x, y):
	colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	maxvalue = max(y[0], y[1], y[2])
	minvalue = min(y[0], y[1], y[2])
	add_value = 1 - maxvalue
	if maxvalue == minvalue:
		# my_colors = [(y[0], y[1], y[2])]
		my_colors = [(y[0]+add_value-0.02, y[1]+add_value-0.02, y[2]+add_value-0.02)]
		# my_colors = [(1, 1, 0)]
		title = "Perfect in allocation"
	elif maxvalue-minvalue < 0.2 and maxvalue-minvalue > 0 and maxvalue-minvalue == 0.2:
		my_colors = [(y[0]+add_value, y[1]+add_value, y[2]+add_value)]
		title = "Good in allocation"
	elif maxvalue-minvalue < 0.5 and maxvalue-minvalue > 0.2 and maxvalue-minvalue == 0.5:
		my_colors = [(y[0]+add_value, y[1]+add_value, y[2]+add_value)]
		title = "Fair in allocation"
	elif maxvalue-minvalue > 0.5:
		my_colors = [(y[0]+add_value, y[1]+add_value, y[2]+add_value)]
		title = "Need improvements in allocation"

	new_y = [1, 0]
	plt.pie(new_y,colors=my_colors)
	plt.xticks(rotation=45)
	plt.tight_layout()
	graph = get_graph()
	return graph


def get_plot4(x, y):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	plt.title('Gender Distribution')
	# my_colors = ['red','blue']
	plt.pie(y,labels=x, autopct='%1.1f%%')
	plt.xticks(rotation=45)
	plt.xlabel('gender')
	plt.ylabel('count')
	plt.tight_layout()
	graph = get_graph()
	return graph



def get_plot5(x, y):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	plt.title('Race Distribution')
	# my_colors = ['red','blue']
	plt.pie(y,labels=x, autopct='%1.1f%%')
	plt.xticks(rotation=45)
	plt.xlabel('race')
	plt.ylabel('count')
	plt.tight_layout()
	graph = get_graph()
	return graph


def get_plot6(x, y):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	plt.title('Family Education Background Distribution')
	# my_colors = ['red','blue']
	plt.pie(y,labels=x, autopct='%1.1f%%')
	plt.xticks(rotation=45)
	plt.xlabel('family education')
	plt.ylabel('count')
	plt.tight_layout()
	graph = get_graph()
	return graph


def get_color_code(gender_percent, race_percent, college_percent):
	gender_rgb = (255 - 1020*(gender_percent-0.5)*(gender_percent-0.5))/256
	race_rgb = (255 - 1020*(race_percent-0.5)*(race_percent-0.5))/256
	college_rgb = (255 -1020*(college_percent-0.5)*(college_percent-0.5))/256
	return [(gender_rgb, race_rgb, college_rgb)]

def get_plot7(gender_percent, race_percent, college_percent):
	color_code = get_color_code(gender_percent, race_percent, college_percent)
	# colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	new_y = [1, 0]
	plt.pie(new_y,colors=color_code)
	graph = get_graph()
	return graph


