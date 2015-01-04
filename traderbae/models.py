from django.db import models

class User(models.Model):
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=10, help_text="This will be your name around the site.")
	account_created = models.DateTimeField('account created')
	school = models.CharField(max_length=50, default='Columbia') 
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=16)
	items = models.IntegerField(max_length=3, default=0)
	photo = models.ImageField(upload_to='users')


class Item(models.Model):
	owner = models.ForeignKey(User)
	brand = models.CharField(max_length=20)
	clothes_choices = (
		('DR','Dresses'),
		('TP','Tops'),
		('BM','Bottoms'),
		('J','Jewelry'),
		('SH','Shoes'),
		('O', 'Other'),
	)	
	article = models.CharField(max_length=2, choices=clothes_choices)
	color = models.CharField(max_length=10)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	likes = models.IntegerField(default=0)
	photo = models.ImageField(upload_to='items')
