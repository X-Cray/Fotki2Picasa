import logging
import urllib
from google.appengine.api import urlfetch
from django.shortcuts import *
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils import simplejson as json
from common import *

# Home page view.
def index(request):
	return render_to_response('mover/index.html', { 'profile': request.user.profile if request.user.is_authenticated() else None })

def login_yandex(request):
	return redirect('https://oauth.yandex.ru/authorize?response_type=code&client_id=%s' % application_key_yandex)

def login_google(request):
	return render_to_response('mover/index.html')

def verify_yandex(request):
	logging.info('Got OAuth redirect: %s' % request.get_full_path())
	error = 'error' in request.GET and request.GET['error']

	if error:
		logging.error('Yandex auth code request error: %s' % error)
	else:
		code = request.GET['code']
		logging.info('Got auth code from Yandex: %s' % code)
		params = {
			'grant_type': 'authorization_code',
			'client_id': application_key_yandex,
			'code': code
		}
		result = urlfetch.fetch(url='https://oauth.yandex.ru/token', payload=urllib.urlencode(params), method=urlfetch.POST)
		if result.status_code == 200:
			data = json.loads(result.content)
			if 'access_token' in data:
				logging.info('Received Yandex access token: %s' % data['access_token'])
				if 'expires_in' in data:
					logging.info('Token expires in %d seconds' % data['expires_in'])
				result = urlfetch.fetch(url='http://api-yaru.yandex.ru/me/?format=json', method=urlfetch.GET, headers={ 'Authorization': 'OAuth %s' % data['access_token'] })
				headers = '; '.join(['%s = %s' % (k, v) for k, v in result.headers.iteritems()])
				logging.debug('Received Yandex response: %d : %s : %s' % (result.status_code, headers, result.content))
				person = json.loads(result.content)
				username = person['name']
				userpic = person['links']['userpic']
				
				# Load existing or create new user.
				try:
					existing_user = User.objects.get(username__exact=username)
				except User.DoesNotExist:
					existing_user = User.objects.create_user(username, 'temp@fotki2picasa.appspot.com', 'password')

				existing_profile = existing_user.profile
				existing_profile.yandex_token = data['access_token']
				existing_profile.yandex_name = username
				existing_profile.yandex_picture = userpic
				existing_profile.save()

				#logging.debug('Profile: %s, %s, %s, %s' % (data['access_token'], username, userpic, person))

				existing_user.backend = 'django.contrib.auth.backends.ModelBackend'
				login(request, existing_user)
			else:
				logging.error('Yandex have not returned the access token: %s' % result.content)
		else:
			logging.error('Yandex token request error: %d' % result.status_code)

	#auth_token = request.get('oauth_token')
	#auth_verifier = request.get('oauth_verifier')

	#		session = Session(writer='cookie')
	#		session['username'] = user_info['username']

	#		user = UserInfo.get_or_insert(user_info['username'])
	#		user.name = user_info['name']
	#		user.picture = user_info['picture']
	#		user.token = user_info['token']
	#		user.secret = user_info['secret']

	#		user.save()
	
	return redirect('/')

def verify_google(request):
	return render_to_response('mover/index.html')

