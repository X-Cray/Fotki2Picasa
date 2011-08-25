from google.appengine.ext import webapp
from common import *

class LoginYandex(webapp.RequestHandler):
	def get(self):
		self.redirect("https://oauth.yandex.ru/authorize?response_type=code&client_id=%s&state=yandex" % application_key_yandex)
