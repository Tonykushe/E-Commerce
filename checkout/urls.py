from django.conf.urls import url
from checkout.views import *

urlpatterns = [
	url(r'^$', checkout, name='checkout'),
	
]


