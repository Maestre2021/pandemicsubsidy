from django.db import models
from django.utils import timezone

class Psrsignup(models.Model):
	firstname = models.CharField(max_length=50, default="", null=True)
	lastname = models.CharField(max_length=50, default="", null=True)
	address = models.TextField(default="")
	occupation_head = models.CharField(max_length=50, default="")
	username = models.CharField(max_length=15, default="", null=True)
	password = models.CharField(max_length=15, default="", null=True)
	

class Psrlogin(models.Model):
	login = models.ForeignKey(Psrsignup, default="", on_delete=models.CASCADE)
	u_name = models.CharField(max_length=50, default="")


class Familyinfo(models.Model):
	login = models.ForeignKey(Psrsignup, default="", on_delete=models.CASCADE)
	familyfirstname = models.CharField(max_length=50, default="", null=True)
	familylastname = models.TextField(default="")
	occupation = models.CharField(max_length=50, default="")
	salary_head = models.IntegerField(default="")
	salary = models.IntegerField(default="")
	total_salary = models.IntegerField(default=None)

class Subsidyconfirmation(models.Model):
	file = models.FileField(blank=True, null=True)
	image =  models.ImageField(blank=True, null=True)
	full_address = models.TextField(default="" )
	contact = models.IntegerField(default="")
	applicant_number = models.IntegerField(default="")
	date = models.DateTimeField(auto_now_add=True)
	family_member = models.IntegerField(default="")
	subsidy = models.IntegerField(default="")

class Receivingplacedate(models.Model):

	PLACE_CHOICES = (
	    ('PTM', 'PTM'),
	    ('Metanoiah', 'Metanoiah'),
	    ('Holy', 'Holy'),
	    ('Court', 'Court'),
	)
	place = models.CharField(max_length=50, default="", choices=PLACE_CHOICES, null=True)
	date = models.DateField(default="")
	time = models.TimeField(default="")

class Receivingbankpawnshop(models.Model):

	BANKPAWN_CHOICES = (
	    ('BDO', 'BDO'),
	    ('PNB', 'PNB'),
	    ('MLHUILLER', 'MLHUILLER'),
	    ('PALAWAN', 'PALAWAN'),
	)

	bank_pawnshop = models.CharField(max_length=50, default="", choices=BANKPAWN_CHOICES, null=True)
	date = models.DateField(default="")
	time = models.TimeField(default="")


# Create your models here.

# class pending
# 	firstname
# 	lastname
# 	phase 

# class item
# 	foreign (pending)
# 	occuption
# 	salary
# 	image
# class familysalary
# 	memr
# 	ocu
# 	salary
# 	total