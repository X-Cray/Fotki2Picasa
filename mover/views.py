from django.shortcuts import *

# Home page view.
def index(request):
	return render_to_response('mover/index.html')

def login_google(request):
	return render_to_response('mover/index.html')

def login_yandex(request):
	return render_to_response('mover/index.html')

