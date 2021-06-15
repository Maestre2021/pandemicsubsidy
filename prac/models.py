from django.db import models
from django.utils import timezone


class Psrsignup(models.Model):
	firstname = models.CharField(max_length=50, default="", null=True)
	lastname = models.CharField(max_length=50, default="", null=True)
	address = models.TextField(default="")
	occupation_head = models.CharField(max_length=50, default="")
	salary_head = models.IntegerField(default="")

class Familyinfo(models.Model):
	familyname1 = models.CharField(max_length=50, default="")
	familyname2 = models.CharField(max_length=50, default="")
	familyname3 = models.CharField(max_length=50, default="")
	occupation1 = models.CharField(max_length=50, default="")
	occupation2 = models.CharField(max_length=50, default="")
	occupation3 = models.CharField(max_length=50, default="")
	salary1 = models.IntegerField(default="")
	salary2 = models.IntegerField(default="")
	salary3 = models.IntegerField(default="")
	total_salary = models.IntegerField(default=None)

class Subsidyconfirmation(models.Model):
	file = models.FileField(blank=True, null=True)
	contact = models.IntegerField(default="")
	date = models.DateTimeField(auto_now_add=True)
	subsidy = models.IntegerField(default="")

class Receivingplacedate(models.Model):
	p_name = models.ForeignKey(Psrsignup, default="", on_delete=models.CASCADE)

	PLACE_CHOICES = (
	    ('Phase 1', 'PHASE1'),
	    ('Phase 2', 'PHASE2'),
	    ('Phase 3', 'PHASE3'),
	    ('Phase 4', 'PHASE 4'),
	)
	place = models.CharField(max_length=50, default="", choices=PLACE_CHOICES, null=True)
	date = models.DateField(default="")
	time = models.TimeField(default="")

class Receivingbankpawnshop(models.Model):
	b_name = models.ForeignKey(Psrsignup, default="", on_delete=models.CASCADE)
	BANKPAWN_CHOICES = (
	    ('Landbank', 'LANDBANK'),
	    ('PNB', 'PNB'),
	    ('MLHUILLER', 'MLHUILLER'),
	    ('PALAWAN', 'PALAWAN'),
	)

	bank_pawnshop = models.CharField(max_length=50, default="", choices=BANKPAWN_CHOICES, null=True)
	date = models.DateField(default="")
	time = models.TimeField(default="")

class PSRStatus(models.Model):
	s_name = models.ForeignKey(Psrsignup, on_delete=models.CASCADE)

	STAT_CHOICE = {
	('RECEIVED', 'received'),
	('PENDING', 'pending'),
	('DENIED', 'denied'),
	}
	stat = models.CharField(max_length=20, default="", choices=STAT_CHOICE)

class Additionalassistance(models.Model):
	a_name = models.ForeignKey('Psrsignup', on_delete=models.CASCADE)
	a_address = models.CharField(max_length=50, default="", null=True)
	contact = models.IntegerField(default="")
	loan = models.IntegerField(default="")

class Inquries(models.Model):
	name = models.CharField(max_length=30, default="")
	comments = models.TextField(default="")
	RATE_CHOICES = {
		('1', 'poor'),
		('2', 'weak'),
		('3', 'good'),
		('4', 'very good'),
		('5', 'excellent'),
	}
	rate = models.CharField(max_length=2, default="", choices =RATE_CHOICES, null=True)


	



# class ApplicantStatus(models.Model);
# 	name = models.ForeignKey(Psrsignup, default="", on_delete=models.CASCADE)
# 	stat = models.CharField(max_length=20, default="")



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