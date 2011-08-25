from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from django.utils import simplejson as json
from common import *

class MovePhotos(webapp.RequestHandler):
	def get(self):
		all_users = UserInfo.all()

		for user in all_users:
			pass
