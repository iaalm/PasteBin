from django.db import models

# Create your models here.

class msg(models.Model):
	id = models.AutoField(primary_key=True)
	#time = models.DateTime()
	status = models.IntegerField()
	text = models.TextField()

