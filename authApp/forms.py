from django import forms
from  .models import *
from django.contrib.auth.models import User


# class UserRegistrationForm(forms.ModelForm):
# 	username = forms.CharField(widget=forms.TextInput())
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	email = forms.CharField(widget=forms.EmailInput())
# 	class Meta:
# 		model = UserProfile
# 		fields = ['username','first_name','password','mobile_number_or_email','last__name', 'gender', 'birthday', 'pronoun', 'optional_gender']


	
# 	def clean_username(self):
# 		uname = self.cleaned_data.get('username')
# 		if User.objects.filter(username=uname).exists():
# 			raise forms.ValidationError('this username already exists')
		
# 		return uname

# 	def clean_email(self):
# 		emai = self.cleaned_data.get('email')
# 		if User.objects.filter(mobile_number_or_email=emai).exists():
# 			raise forms.ValidationError('this email or number already exists')
# 		return emai

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())