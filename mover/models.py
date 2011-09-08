from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# This field is required.
	user = models.OneToOneField(User)

	# User names and avatars.
	yandex_name = models.CharField(max_length=100)
	yandex_picture = models.CharField(max_length=200)
	google_name = models.CharField(max_length=100)
	google_picture = models.CharField(max_length=200)

	# Authentication tokens.
	yandex_token = models.CharField(max_length=100)
	yandex_secret = models.CharField(max_length=100)
	google_token = models.CharField(max_length=100)
	google_secret = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.user.username

class MoveArrangement(models.Model):
	user = models.ForeignKey(User)

