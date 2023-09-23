from django.db import models
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Theme(models.Model):
	theme = models.CharField(max_length = 5, null = True)
	def __str__(self):
		return self.theme
