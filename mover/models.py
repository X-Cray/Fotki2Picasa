from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# This field is required.
	user = models.ForeignKey(User, unique=True)

	# User names and avatars.
	yandex_name = models.TextField()
	yandex_picture = models.TextField()
	google_name = models.TextField()
	google_picture = models.TextField()

	# Authentication tokens.
	yandex_token = models.TextField()
	google_token = models.TextField()
	google_secret = models.TextField()
	
	def __unicode__(self):
		return self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class MoveArrangement(models.Model):
	user = models.ForeignKey(User)
