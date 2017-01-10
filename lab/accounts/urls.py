from django.conf.urls import url
from accounts.views import UserRegistrationView
from . import views

urlpatterns = [
	url(r'^$', UserRegistrationView.as_view(), name = 'user-registration'),
	# url(r'^signup/$', UserRegistrationView.as_view(), name = 'user-registration'),
	url(r'^success/$', views.success, name = 'success'),
]