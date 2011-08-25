from google.appengine.ext import db

class UserInfo(db.Model):
	yandex_name = db.StringProperty()
	yandex_picture = db.StringProperty()
	google_name = db.StringProperty()
	google_picture = db.StringProperty()
	yandex_token = db.StringProperty()
	yandex_secret = db.StringProperty()
	google_token = db.StringProperty()
	google_secret = db.StringProperty()

class MoveArrangement(db.Model):
	yandex_name = db.StringProperty()
