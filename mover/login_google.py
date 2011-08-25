from google.appengine.ext import webapp
from common import *

class LoginGoogle(webapp.RequestHandler):
	def get(self):
		self.redirect()
