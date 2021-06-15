from django.urls import path
from . import views 

urlpatters = [
	path("registration", views.register, name="register"),

]