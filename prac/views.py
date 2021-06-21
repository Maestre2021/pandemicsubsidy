from django.shortcuts import render
from prac.models import Psrsignup, Familyinfo, Subsidyconfirmation, Receivingplacedate, Receivingbankpawnshop, PSRStatus, Additionalassistance, Inquries
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def Main(request):
	return render(request, 'psrform.html')

def Home(request):
	return render(request, 'psrform.html')

def Subsidy(request):
	return render(request, 'subsidypage.html')

def Applicant(request):
	return render(request,'applicantpage.html')

def New(request):
	pname = Psrsignup.objects.create(
		firstname =request.POST['firstname'],
		lastname = request.POST['surname'],
		address = request.POST['address'],
		salaryhead = request.POST['salary'],
		occupationhead = request.POST['occupation'],

		)

	return redirect(f'/prac/{pname.id}/')
	
def View(request, pname):
	pname = Psrsignup.objects.get(id=pname)
	return render(request, 'psrlist.html', {'pname': pname })


def Aboutus(request):

	return render(request,'aboutus.html')


def Status(request):
	return render(request,'status.html')


def Assistance(request):
	return render(request,'additionalassistance.html')

def Inquiries(request):

	inquire = Inquiries.objects.create(
			inquire = inquire, 
			iname=request.POST['nameinquiries'], 
			icontact=request.POST['contactinquiries'], 
			rate=request.POST['typemessage'],
			comments=request.POST['message'],
			)

	return redirect(f'/prac/{inquire.id}/')

def addinquire(request, inquirie):
		inquire = Inquiries.objects.get(id=inquire)
		return redirect(f'/prac/{inquire.id}/')

def viewinquire(request, inquire):

		inquire = Inquires.objects.get(id=inquire)
		return render(request, 'inquiresandcomments.html', {'inquire': inquire, 'iname':'nameinquiries',
			'icontact':'contactinquiries',
			'rate': 'typemessage',
			'comments':'message',
			})


# def manipulationofdata():

# 	pname = pendingname(fname="Rabiya Mateo", faddress="Iloilo City", age="23", gender="Female")
# 	pname.save()

# 	objects = pendingname.objects.all()
# 	rslt = 'Printing all entries in pendingname model : <br>'
# 	for x in objects:
# 		res+= x.fname+"<br"


# 	nname = pendingname.objects.get(id="anne")
# 	res += 'Printing One entry <b>'
# 	res += nname.address

# #delete
# 	res += '<br>Deleting an entry<br>'
# 	nname.delete()






# def addItem(request, pn):
# 	pn = Psrsignup.objects.get(id=pn)
# 	Item.objects.create(pname=pn,text=request.POST['surname'], address=request.POST['address'])


# 	return redirect(f'/prac/{pn.id}/')






























# def Main(request):
# 	# firstdata = pendingname.objects.create()
# 	return render(request, 'psrform.html')
# def View(request, pname):
# 	pn = pendingname.objects.get(id=pname)
# 	return render(request, 'psrlist.html', {'pn': pn, 'address': 'address'}) #PINALTAN KO RIN PANG TRY LANG

# def New(request):
# 	newName = pendingname.objects.create()
# 	Item.objects.create(pname=newName, text=request.POST['surname'], address=request.POST['address'])
# 	return redirect(f'/prac/{newName.id}/') #variablename

# 	# money = income.objects.create()
# 	# Money.objects.create(mney=money, occu=request.POST['occu'], salary=request.POST['salary'])
# 	# return redirect(f'/prac/{money.id}/')

# def addItem(request, pname):
# 	pn = pendingname.objects.get(id=pname)
# 	Item.objects.create(pname=pn, text=request.POST['surname'], address=request.POST['address'])
# 	return redirect(f'/prac/{pn.id}/')

# 	# my = income.objects.get(id=mney)
# 	# Money.objects.create(mney=my, occu=request.POST['occu'], salary=request.POST['salary'])
# 	# return redirect (f'/prac/{my.id}/')



# def manipulationofdata():


#1

	# my = income.objects.get(id=mney)




#3

	#	# money = income.objects.create()
	# Money.objects.create(mney=money, occu=request.POST['occu'], salary=request.POST['salary'])
	# return redirect(f'/prac/{money.id}/')



#4
	# my = income.objects.get(id=mney)
	# Money.objects.create(mney=my, occu=request.POST['occu'], salary=request.POST['salary'])
	# return redirect (f'/prac/{my.id}/')










# address=request.POST['address'])

	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['surname'])
	# 	return redirect('/psr/viewlist_url/')

	# return render(request, 'psrform.html', {'sname' : items})


	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['surname'])
	# 	return redirect('/psrform/viewlist_url')




	#return render(request,'psrform.html')

#def Main(request):
	# 	if request.method == 'POST':
	# 	newIt = request.POST['surname']
	# 	Item.objects.create(text=newIt)
	# else:
	# 	newIt = ''
	# return render(request,'psrform.html',{'sname' : newIt,})

	# item1 = Item()
	# item1.text=request.POST.get('surname', '')
	# return render(request,'psrform.html',{'sname': item1.text ,})


	# item1.save()
	# item2 = Item()
	# item2.text=request.POST.get('givenname', '')
	# item2.save()

	#return render(request,'psrform.html',{'sname':request.POST.get('surname') ,'gname': request.POST.get('givenname',''),})

"""def Main(request):
	if request.method == 'POST':
		return HttpResponse(request.POST['surname'])
	return render(request,"psrform.html")

	def Main(request):
	return render(request,'psrform.html',{'sname':request.POST.get('surname') ,'gname': request.POST.get('givenname',''),})"""

 
# Create your views here.
