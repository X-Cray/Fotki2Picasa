from django.shortcuts import *
from common import *

# Home page view.
def index(request):
	return render_to_response('mover/index.html')

def login_yandex(request):
	return redirect('https://oauth.yandex.ru/authorize?response_type=code&client_id=%s' % application_key_yandex)

def login_google(request):
	return render_to_response('mover/index.html')

def verify_yandex(request):
	return render_to_response('mover/index.html')

def verify_google(request):
	return render_to_response('mover/index.html')
