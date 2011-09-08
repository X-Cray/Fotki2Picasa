from django.conf.urls.defaults import *

urlpatterns = patterns('mover.views',
	(r'^$', 'index'),
	(r'^login-yandex/$', 'login_yandex'),
	(r'^login-google/$', 'login_google'),
	(r'^verify-yandex/$', 'verify_yandex'),
	(r'^verify-google/$', 'verify_google')
)
