from django.db import models
from django.contrib.auth.models import User

# Model to define the company object
class Company(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

# Model to define the Data Layer object
# Data Layer has 1-1 relationship with company
class DataLayer(models.Model):
	company = models.OneToOneField(Company)

	def __str__(self):
		return self.company.name

# Model to define a data table
# There can be n data tables in a data layer
class DataTable(models.Model):
	name = models.CharField(max_length=100)
	dataLayer = models.ForeignKey('DataLayer')
	creationDate = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Creation date")
	updateDate = models.DateTimeField(auto_now=True, verbose_name="Last Update Date")

	def __str__(self):
		return self.name

# Model to extend the user object in order to make the link with the company object. (User belongs to a company)
class Profile(models.Model):
	user = models.OneToOneField(User)
	company = models.OneToOneField(Company)

	def __str__(self):
		return self.user.username