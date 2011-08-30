from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'index'),
	(r'^/login-yandex$', 'login_yandex'),
	(r'^/login-google$', 'login_google')
)
