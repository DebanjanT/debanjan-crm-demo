from django.db import models

#Customer Model
class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True) 

	def __str__(self):
		return self.name

#for tags ManytoMany relationship
class Tag(models.Model):
	name = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.name


#Product Model
class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description =models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	tag = models.ManyToManyField(Tag) 

	def __str__(self):
		return self.name



#Order Model
class Order(models.Model):
	DELIVERY_STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			  )
	PAYMENT_STATUS = (
			('Cash On Delivery', 'Cash On Delivery'),
			('Net Banking', 'Net Banking'),
			('EMI', 'EMI'),
			  )
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True) #one to many rltnshp
	product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True) #one to many rltnshp
	date_created = models.DateTimeField(auto_now_add=True,null=True) 
	dstatus = models.CharField(max_length=200, null=True, choices=DELIVERY_STATUS)
	pstatus = models.CharField(max_length=200,null=True,choices=PAYMENT_STATUS)

	def __str__(self):
		return self.product.name


	