from django.contrib.auth.base_user import BaseUserManager
# import pdb

class UserManager(BaseUserManager):
	"""
	Manager for custom user model
	"""
	
	use_in_migrations = True
	
	def create_user(self, email, first_name, last_name, password, **kwargs):
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			is_active = True,
			is_staff = False,
			**kwargs
		)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, first_name, last_name, password, **kwargs):
		user = self.model(
			email = self.normalize_email(email),
			first_name = "",
			last_name = "",
			is_staff = True,
			is_active = True,
			is_superuser = True,
			**kwargs
		)
		user.set_password(password)
		user.save(using = self._db)
		return user