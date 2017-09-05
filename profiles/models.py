from django.db import models

# Create your models here.
class Profile(models.Model):
	name        = models.CharField(max_length=120, default='')
	description = models.TextField(default='Add a description')

	def __str__(self):
		return self.name
		