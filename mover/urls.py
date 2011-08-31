from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'mover.views.index'),
	(r'^/login-yandex$', 'mover.views.login_yandex'),
	(r'^/login-google$', 'mover.views.login_google')
)
