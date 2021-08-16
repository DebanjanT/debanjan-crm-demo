import django_filters
from .models import *

class orderFilter(django_filters.FilterSet):
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer','date_created']
