from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from . managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
	"""
	Class that presents user of the nostroweb

	The unique field is email
	"""
	
	email = models.EmailField(unique = True, blank = False)

	is_active = models.BooleanField(default = False)

	is_staff = models.BooleanField(default = False)

	objects = UserManager()

	first_name = models.CharField(max_length = 15, default = "", null = True)

	last_name = models.CharField(max_length = 15, default = "", null = True)

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'

	USERNAME_FIELD = 'email'

	def get_full_name():
		return email

	def get_short_name():
		return email