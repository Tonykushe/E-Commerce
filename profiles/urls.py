from django.conf.urls import url
from profiles.views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^about/$', about, name='about'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^profile/$', profile, name='profile'),
]


