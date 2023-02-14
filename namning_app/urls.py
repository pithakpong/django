from django.urls import path 
from .views import *
urlpatterns = [ 
	path('members/',members,name='members'), 
	path('',details,name='details'),
	path('members/branch/<int:id>',branch,name='branch'),
	path('tests',test,name='tests'),
]