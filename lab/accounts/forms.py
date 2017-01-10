from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.password_validation import validate_password

from . models import User

class DateInput(forms.DateInput):
	input_type = 'date'

class EmailInput(forms.TextInput):
	def render(self, name, value, attrs = None):
		if attrs:
			attrs['oninput'] = 'ValidateEmail()'
			attrs['id'] = 'id_' + name
		else:
			attrs = {
				'oninput' : 'ValidateEmail()',
				'id' : 'id_' + name,
				}
		output = super(EmailInput, self).render(name, value, attrs)
		return output


class UserRegistrationForm(forms.ModelForm):
	"""
	A form for creating new users. Include all the required
	fields, plus a repeated password.
	"""

	error_css_class = 'error'
	# required_css_class = 'required'

	password = forms.CharField(label = 'Password', widget = forms.PasswordInput()) # (attrs = { 'oninput' : 'ValidatePassword()'}))
	
	# password2 = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('email',)
		widgets = {
			'email': forms.TextInput() # attrs = { 'oninput' : 'ValidateEmail()' })
		}

	def clean_email(self):
		"""
		Return lowercase email
		"""
		email = self.cleaned_data.get('email')
		return email.lower()

	def save(self, commit = True):
		"""
		Save the provided password in hashed format
		"""
		user = super(UserRegistrationForm, self).save(commit = False)
		user.set_password(self.cleaned_data['password'])
		user.is_active = True
		user.is_stuff = False
		if commit:
			user.save()
		return user