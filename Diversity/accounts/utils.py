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
	plt.title('Chart')
	plt.pie(y,labels=x,autopct='%1.1f%%')
	plt.xticks(rotation=45)
	plt.xlabel('category')
	plt.ylabel('count')
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
	# by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
 #                for name, color in colors.items())
	# sorted_names = [name for hsv, name in by_hsv]
	plt.switch_backend('AGG')
	plt.figure(figsize=(10, 5))
	maxvalue = max(y[0], y[1], y[2])
	minvalue = min(y[0], y[1], y[2])
	if maxvalue == minvalue:
		# my_colors = [(y[0], y[1], y[2])]
		my_colors = [(y[0]*2.5, y[1]*2.5, y[2]*2.5)]
	elif maxvalue-minvalue < 0.2 and maxvalue-minvalue > 0 and maxvalue-minvalue == 0.2:
		my_colors = [(y[0]*2.5, y[1]*2.5, y[2]*2.5)]
	elif maxvalue-minvalue < 0.5 and maxvalue-minvalue > 0.2 and maxvalue-minvalue == 0.5:
		my_colors = [(y[0]*2.5, y[1]*2.5, y[2]*2.5)]
	elif maxvalue-minvalue > 0.5:
		my_colors = [(y[0]*2.5, y[1]*2.5, y[2]*2.5)]

	new_y = 1
	# color=colors.reshape(-1,4)
	#plt.pie(new_y,colors=my_colors)
	# plt.pie(new_y,color=my_colors.reshape(-1, 4))
	# plt.plot([1,2], lw=4, c='xkcd:baby poop green')
	plt.xticks(rotation=45)
	plt.tight_layout()
	graph = get_graph()
	return graph
	# return graph





