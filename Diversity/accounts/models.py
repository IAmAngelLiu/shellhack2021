from django.db import models

# Create your models here.


class Employee(models.Model):
	GENDER = (
		('Female', 'Female'),
		('Male', 'Male'),
		('Others', 'Others'),
		('Not disclosed', 'Not disclosed'),
		)
	RACE = (
		('White', 'White'),
		('Asian', 'Asian'),
		('Black', 'Black'),
		('American Indian', 'American Indian'),
		('Hispanic', 'Hispanic'),
		('Others', 'Others'),
		)
	FIRSTCOLLEGE = (
		('Yes', 'Yes'),
		('No', 'No'),
		)
	name = models.CharField(max_length=100, null=True)
	gender = models.CharField(max_length=100, null=True, choices=GENDER)
	race = models.CharField(max_length=100, null=True, choices=RACE)
	firstcollege = models.CharField(max_length=100, null=True, choices=FIRSTCOLLEGE)
	data_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



class Data(models.Model):
	CATEGORY = (
		('Gender', 'Gender'),
		('Race', 'Race'),
		('firstcollege', 'firstcollege'),
		)
	category = models.CharField(max_length=100, null=True, choices=CATEGORY)
	points = models.IntegerField(null=True)



class Points(models.Model):
	TYPE = (
		('Female', 'Female'),
		('Black', 'Black'),
		('American Indian', 'American Indian'),
		('Hispanic', 'Hispanic'),
		('firstcollege', 'firstcollege'),
		)
	category = models.CharField(max_length=100, null=True, choices=TYPE)
	points = models.IntegerField(null=True)













