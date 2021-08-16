from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class orderForm(ModelForm):
	class Meta:
		model = Order #database model
		fields = '__all__' #['customer', 'dstatus'] for specific  

class customerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


class createUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
