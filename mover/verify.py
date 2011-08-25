import logging
import urllib
from django.utils import simplejson as json
from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from appengine_utilities.sessions import Session
from common import *

class VerifyPage(webapp.RequestHandler):
	def get(self):
		logging.info("Got OAuth redirect: %s" % self.request.query_string)
		is_yandex = self.request.get("state") == "yandex"
		
		if is_yandex:
			error = self.request.get("error")
			if error:
				logging.error("Yandex auth code request error: %s" % error)
			else:
				code = self.request.get("code")
				logging.info("Got auth code from Yandex: %s" % code)
				params = {
					"grant_type": "authorization_code",
					"client_id": application_key_yandex,
					"code": code
				}
				result = urlfetch.fetch(url="https://oauth.yandex.ru/token", payload=urllib.urlencode(params), method=urlfetch.POST)
				if result.status_code == 200:
					data = json.loads(result.content)
					if "access_token" in data:
						logging.info("Received Yandex access token: %s" % data["access_token"])
						result = urlfetch.fetch(url="http://api-fotki.yandex.ru/api/me/", method=urlfetch.GET, headers={ "Authorization": "OAuth %s" % data["access_token"]})
						headers = "; ".join(["%s = %s" % (k, v) for k, v in result.headers.iteritems()])
						logging.info("Received Yandex response: %d : %s : %s" % (result.status_code, headers, result.content))
					else:
						logging.error("Yandex did not return the access token: %s" % result.content)
				else:
					logging.error("Yandex token request error: %d" % result.status_code)

		auth_token = self.request.get("oauth_token")
		auth_verifier = self.request.get("oauth_verifier")

#		self.session = Session(writer="cookie")
#		self.session["username"] = user_info["username"]

#		user = UserInfo.get_or_insert(user_info["username"])
#		user.name = user_info["name"]
#		user.picture = user_info["picture"]
#		user.token = user_info["token"]
#		user.secret = user_info["secret"]

#		user.save()

		self.redirect('/')
