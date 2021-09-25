import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

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





