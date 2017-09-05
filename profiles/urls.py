from django.conf.urls import url
from profiles.views import *

urlpatterns = [
	url(r'^$', home, name='home')
]


