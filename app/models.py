from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
	user = models.OneToOneField(User)
	edad = models.IntegerField(null=False, blank=False)

	def __unicode__(self):
		return self.user.username