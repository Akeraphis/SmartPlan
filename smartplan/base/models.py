from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class DataLayer(models.Model):
	company = models.OneToOneField(Company)

	def __str__(self):
		return self.id


class DataTable(models.Model):
	name = models.CharField(max_length=100)
	dataLayer = models.ForeignKey('DataLayer')
	creationDate = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Creation date")
	updateDate = models.DateTimeField(auto_now=True, verbose_name="Last Update Date")

	def __str__(self):
		return self.name