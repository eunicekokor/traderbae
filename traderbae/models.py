import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=18, help_text="This will be your name around the site.")
	account_created = models.DateTimeField(default=timezone.now())
	school = models.CharField(max_length=50, default='Columbia') 
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=16)
	items = models.IntegerField(max_length=3, default=0)
	photo = models.ImageField(upload_to='users')
	def new_user(self):
		return self.account_created >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return '%s, username: %s' % (self.name, self.username)

class Item(models.Model):
	owner = models.ForeignKey(User)
	brand = models.CharField(max_length=20)
	date_added = models.DateTimeField('date added')
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
	#photo = models.ImageField(upload_to='items')
	def __str__(self):
		return '%s %s' % (self.brand, self.article)
	def new_item(self):
		return self.date_added >= timezone.now() - datetime.timedelta(days=2)
	def hot_item(self):
		return self.likes >= 5