from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# This field is required.
	user = models.ForeignKey(User, unique=True)

	# User names and avatars.
	yandex_name = models.CharField(max_length=100, blank=True)
	yandex_picture = models.CharField(max_length=200, blank=True)
	google_name = models.CharField(max_length=100, blank=True)
	google_picture = models.CharField(max_length=200, blank=True)

	# Authentication tokens.
	yandex_token = models.CharField(max_length=100, blank=True)
	google_token = models.CharField(max_length=100, blank=True)
	google_secret = models.CharField(max_length=100, blank=True)
	
	def __unicode__(self):
		return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class MoveArrangement(models.Model):
	user = models.ForeignKey(User)
