from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'fotki2picasa.views.home', name='home'),
	# url(r'^fotki2picasa/', include('fotki2picasa.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	(r'^_ah/warmup$', 'djangoappengine.views.warmup'),
	(r'^admin/', include(admin.site.urls)),
	(r'^', include('fotki2picasa.mover.urls')),
)
